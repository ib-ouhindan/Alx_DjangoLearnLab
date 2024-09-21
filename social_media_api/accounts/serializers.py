from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    token = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'token']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        token, created = Token.objects.create(user=user)
        user.token = token.key
        return user


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
