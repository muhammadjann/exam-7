from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password", "phone_number"]
        extra_kwargs = {"password": {"write_only": True}}
