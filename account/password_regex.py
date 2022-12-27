import re
from rest_framework import serializers


def password_re(password):
    if len(password) < 8:
        raise serializers.ValidationError('password must be at least 8 characters')
    is_valid = re.search('[A-Z]', password)
    if not is_valid:
        raise serializers.ValidationError('password must be contains at least one uppercase')
    is_valid = re.search('[a-z]', password)
    if not is_valid:
        raise serializers.ValidationError('password must be contains at least one lowercase')
    is_valid = re.search('\\d', password)
    if not is_valid:
        raise serializers.ValidationError('password must be contains at least one digit')
    is_valid = re.search('\\W', password)
    if not is_valid:
        raise serializers.ValidationError('password must be contains at least one special character')
    not_valid = re.search('\\s', password)
    if not_valid:
        raise serializers.ValidationError('password must not be contains space')
    return password
