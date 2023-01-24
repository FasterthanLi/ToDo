from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response

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
