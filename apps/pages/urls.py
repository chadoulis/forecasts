from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    #Gerenal Pages
    path('', TemplateView.as_view(template_name="page/Home.html")),
    path('about/', TemplateView.as_view(template_name="page/About.html")),
    path('team/', TemplateView.as_view(template_name="page/Team.html")),
    path('terms-and-conditions/', TemplateView.as_view(template_name="page/TermsAndConditions.html")),
    path('privacy-policy/', TemplateView.as_view(template_name="page/PrivacyPolicy.html")),

    #Registration and password pages
    path('login/', TemplateView.as_view(template_name="page/Login.html")),
    path('register/', TemplateView.as_view(template_name="page/Register.html")),
    path('forgot-password/', TemplateView.as_view(template_name="page/ForgotPassword.html")),    
    path('reset-password/<str:TempToken>', TemplateView.as_view(template_name="page/ResetPassword.html")),                        
    path('confirm-account/<str:TempToken>', TemplateView.as_view(template_name="page/ConfirmAccount.html")),                        
    
    #Account pages    
    path('account/', TemplateView.as_view(template_name="page/Account.html")),
    path('account/groups/', TemplateView.as_view(template_name="page/AccountGroups.html")),
    path('account/settings/', TemplateView.as_view(template_name="page/AccountSettings.html")),


  
    
]
