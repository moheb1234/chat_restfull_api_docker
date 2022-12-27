from rest_framework import serializers

from message.models import Message


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['sender', 'send_date']

    def create(self, validated_data):
        sender = self.context['request'].user
        validated_data['sender'] = sender
        message = Message.objects.create(**validated_data)
        message.save()
        return message


class UpdateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['sender', 'receiver', 'send_date']
