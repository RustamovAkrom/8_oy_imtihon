from rest_framework import serializers
from apps.task1.models import User
from rest_framework.exceptions import ValidationError
from apps.task1.utils import random_string


class UserCreateSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise ValidationError("passwords don't match")
        return attrs

    def create(self, validated_data):
        username = validated_data.get("username")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        email = validated_data.get("email")
        password = validated_data.get("password1")
        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            token=random_string(),
        )
        user.set_password(password)
        user.save()
        return validated_data

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
