from rest_framework import serializers
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.conf import settings
from . import models
from .tasks import send_email_signup_success


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ("email", "username", "date_joined")
        extra_kwargs = {"date_joined": {"read_only": True}}


class UserCreateSerializer(UserSerializer):
    conf_password = serializers.CharField(
        trim_whitespace=False, max_length=128, write_only=True
    )

    class Meta:
        model = UserSerializer.Meta.model
        fields = UserSerializer.Meta.fields + ("password", "conf_password")
        extra_kwargs = UserSerializer.Meta.extra_kwargs | {
            "password": {"write_only": True},
            "conf_password": {"write_only": True},
        }

    def validate(self, attrs):
        password = attrs["password"]
        conf_password = attrs.pop("conf_password")

        try:
            password_validation.validate_password(password, None)
        except ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        if conf_password is None or password != conf_password:
            raise serializers.ValidationError({"conf_password": " Пароли не совпадают"})

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        if not settings.TESTING:
            send_email_signup_success.delay(validated_data["email"])
        return user
