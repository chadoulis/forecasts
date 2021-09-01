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

    #Group pages    
    path('group/<str:GroupID>/', TemplateView.as_view(template_name="page/Group.html")),
    path('group/<str:GroupID>/members/', TemplateView.as_view(template_name="page/GroupMembers.html")),
    path('group/<str:GroupID>/members/add/', TemplateView.as_view(template_name="page/GroupMembersAdd.html")),    
    path('group/<str:GroupID>/bets/', TemplateView.as_view(template_name="page/GroupBets.html")),
    path('group/<str:GroupID>/bets/active/', TemplateView.as_view(template_name="page/GroupBetsActive.html")),
    path('group/<str:GroupID>/bets/completed/', TemplateView.as_view(template_name="page/GroupBetsCompleted.html")),
    path('group/<str:GroupID>/bets/create/', TemplateView.as_view(template_name="page/GroupBetsCreate.html")),
    path('group/<str:GroupID>/bet/<str:BetID>', TemplateView.as_view(template_name="page/GroupBet.html")),
    path('group/<str:GroupID>/bet/<str:BetID>/add/', TemplateView.as_view(template_name="page/GroupBetAdd.html")),
     
]
