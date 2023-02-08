from django.urls import path, include
from .views import GetView, LoginView, LogoutView, PasswordChangeView, SignUpView
from django.urls import path


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('get-view/', GetView.as_view(), name='get-view'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('passwordchange/', PasswordChangeView.as_view(), name='logout'),
    path('SignUp/', SignUpView.as_view(), name='signUp'),
]