from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="page/Home.html")),
    path('about/', TemplateView.as_view(template_name="page/About.html")),
    path('login/', TemplateView.as_view(template_name="page/Login.html")),
    path('register/', TemplateView.as_view(template_name="page/Register.html")),
    path('team/', TemplateView.as_view(template_name="page/Team.html")),
    path('terms-and-conditions/', TemplateView.as_view(template_name="page/TermsAndConditions.html")),
    path('privacy-policy/', TemplateView.as_view(template_name="page/PrivacyPolicy.html"))

    
]
