from django.core.validators import RegexValidator
from django.utils import timezone
from rest_framework import serializers


def validate_username_regexp():
    return RegexValidator(r'^[\w.@+-]+')


def validate_user_username(value):
    if value.lower() == 'me':
        raise serializers.ValidationError(
            'Вы не можете зарегистрировать имя me/Me/ME/mE')
    return value


def validate_title_year(value):
    if value > timezone.now().year:
        raise serializers.ValidationError(
            'Год больше текущего!'
        )
