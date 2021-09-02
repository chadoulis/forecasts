from django.urls import path
from django.views.generic import TemplateView
from forecasts.pages.views import HomeView, AboutView, TeamView , TermsAndConditionsView , PrivacyPolicyView

urlpatterns = [
    #General Pages
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view()),
    path('team/', TeamView.as_view()),
    path('terms-and-conditions/', TermsAndConditionsView.as_view()),
    path('privacy-policy/', PrivacyPolicyView.as_view()),

]
