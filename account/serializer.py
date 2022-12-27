from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from rest_framework import serializers

from .password_regex import password_re


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, max_length=40)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        del validated_data['confirm_password']
        return User.objects.create(**validated_data)

    def validate(self, attrs):
        if not check_password(attrs['confirm_password'], attrs['password']):
            raise serializers.ValidationError('password dont match')
        return attrs

    def validate_password(self, value):
        return make_password(password_re(value))


class UserChangePasswordSerializer(serializers.Serializer):  # noqa
    old_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if not attrs['password'] == attrs['confirm_password']:
            raise serializers.ValidationError('new password not match')
        return attrs

    def validate_old_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('password is wrong')
        return value

    def validate_password(self, value):
        return password_re(value)

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
