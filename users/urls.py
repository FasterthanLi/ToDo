from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GetView, LoginView, LogoutView, PasswordChangeView
from rest_framework.authtoken import views
from django.urls import path


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('get-view/', GetView.as_view(), name='get-view'),
    path('Logout/', LogoutView.as_view(), name='logout'),
    path('passwordchange/', PasswordChangeView.as_view(), name='logout'),
]