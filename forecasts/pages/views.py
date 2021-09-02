from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

#General views
class HomeView(TemplateView):
    template_name = "main_templates/Home.html"
class AboutView(TemplateView):
    template_name = "main_templates/About.html"
class TeamView(TemplateView):
    template_name = "main_templates/Team.html"
class TermsAndConditionsView(TemplateView):
    template_name = "main_templates/TermsAndConditions.html"  
class PrivacyPolicyView(TemplateView):
    template_name = "main_templates/PrivacyPolicy.html"
