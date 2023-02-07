from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import serializers
from rest_framework import views
from rest_framework import permissions
from rest_framework import status
from .serializers import LoginSerializer
from django.contrib.auth import logout


class GetView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        data = {
            'message': 'Hello, you are authenticated!',
            'email': request.user.email,
            'phone_number': request.user.phone_number,

        }
        return Response(data)

class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return Response(status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"error": "Login failed"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)