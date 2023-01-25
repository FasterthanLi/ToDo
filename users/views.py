from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(self.request.data['password'])
        user.save()


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        phone_number = request.data.get("phone_number")
        password = request.data.get("password")
        user = authenticate(request, email=email, phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            return Response(status=200, data={"detail":"Success"})
        else:
            return Response(status=400, data={"detail":"Invalid credentials"})
