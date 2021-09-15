from django.urls import path
from forecasts.users.views import *


# "www.xxx.com/user" is defined at main urls.py

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/<str:username>', ProfileView.as_view(),
         name='profile_plus_username'),
    path('forgot-password/', ForgotPasswordView.as_view()),
    path('reset-password/<str:TempToken>', CustomPasswordResetView.as_view()),
    path('confirm-account/<str:TempToken>', ConfirmAccountView.as_view()),
]
