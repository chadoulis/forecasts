from django.urls import path
from django.views.generic import TemplateView
from forecasts.pages.views import *

urlpatterns = [
    #General Pages
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view()),
    path('team/', TeamView.as_view()),
    path('terms-and-conditions/', TermsAndConditionsView.as_view()),
    path('privacy-policy/', PrivacyPolicyView.as_view()),

    # Registration and password pages
    # Moved to users

    #Account pages 
    path('account/', AccountView.as_view()),
    path('account/groups/', AccountGroupsView.as_view()),
    path('account/settings/', AccountSettingsView.as_view()),

    #Group pages    
    path('group/<str:GroupID>/', GroupView.as_view()),
    path('group/<str:GroupID>/members/', GroupMembersView.as_view()),
    path('group/<str:GroupID>/members/add/', GroupMembersAddView.as_view()),
    path('group/<str:GroupID>/bets/', GroupBetsView.as_view()),
    path('group/<str:GroupID>/bets/active/', GroupBetsActiveView.as_view()),
    path('group/<str:GroupID>/bets/completed/', GroupBetsCompletedView.as_view()),
    path('group/<str:GroupID>/bets/create/', GroupBetsCreateView.as_view()),
    path('group/<str:GroupID>/bet/<str:BetID>', GroupBetView.as_view()),
    path('group/<str:GroupID>/bet/<str:BetID>/add/', GroupBetAddView.as_view()),

    #Test pages    
    path('example/component/<str:componentName>/', ExampleView.component),
]
