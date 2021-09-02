from django.urls import path
from django.views.generic import TemplateView
from forecasts.pages.views import HomeView, AboutView, TeamView , TermsAndConditionsView , PrivacyPolicyView
from forecasts.pages.views import LoginView, RegisterView, ForgotPasswordView, ResetPasswordView, ConfirmAccountView
from forecasts.pages.views import AccountView, AccountGroupsView, AccountSettingsView

urlpatterns = [
    #General Pages
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view()),
    path('team/', TeamView.as_view()),
    path('terms-and-conditions/', TermsAndConditionsView.as_view()),
    path('privacy-policy/', PrivacyPolicyView.as_view()),

    #Registration and password pages
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('forgot-password/', ForgotPasswordView.as_view()),    
    path('reset-password/<str:TempToken>', ResetPasswordView.as_view()),                        
    path('confirm-account/<str:TempToken>', ConfirmAccountView.as_view()),     

    #Account pages 
    path('account/', AccountView.as_view()),
    path('account/groups/', AccountGroupsView.as_view()),
    path('account/settings/', AccountSettingsView.as_view()),
]
