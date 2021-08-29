from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "pages/about.html"


class HomeView(TemplateView):
    template_name = "pages/home.html"