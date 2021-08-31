from django.urls import path
from django.views.generic import TemplateView
from forecasts.pages.views import AboutView, HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view()),
]
