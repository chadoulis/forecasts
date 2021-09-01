from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="page/Home.html")),
    path('about/', TemplateView.as_view(template_name="page/About.html")),
    path('register/', TemplateView.as_view(template_name="page/Register.html")),
    path('team/', TemplateView.as_view(template_name="page/Team.html")),
    path('terms/', TemplateView.as_view(template_name="page/Terms.html"))
]
