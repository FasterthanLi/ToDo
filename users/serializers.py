from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'phone_number', 'is_active', 'is_admin', 'is_staff', 'is_superuser')

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(style={'input_type': 'password'},required=True)
    new_password = serializers.CharField(style={'input_type': 'password'}, required=True)
    confirm_new_password = serializers.CharField(style={'input_type': 'password'}, required=True)
