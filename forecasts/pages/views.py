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

#Registration and password views
class LoginView(TemplateView):
    template_name = "main_templates/Login.html"
class RegisterView(TemplateView):
    template_name = "main_templates/Register.html"
class ForgotPasswordView(TemplateView):
    template_name = "main_templates/ForgotPassword.html"
class ResetPasswordView(TemplateView):
    template_name = "main_templates/ResetPassword.html"
class ConfirmAccountView(TemplateView):
    template_name = "main_templates/ConfirmAccount.html"

 #Account pages views
class AccountView(TemplateView):
    template_name = "main_templates/Account.html"
class AccountGroupsView(TemplateView):
    template_name = "main_templates/AccountGroups.html"
class AccountSettingsView(TemplateView):
    template_name = "main_templates/AccountSettings.html"

#Group pages views
class GroupView(TemplateView):
    template_name = "main_templates/Group.html"
class GroupMembersView(TemplateView):
    template_name = "main_templates/GroupMembers.html"
class GroupMembersAddView(TemplateView):
    template_name = "main_templates/GroupMembersAdd.html"
class GroupBetsView(TemplateView):
    template_name = "main_templates/GroupBets.html"
class GroupBetsActiveView(TemplateView):
    template_name = "main_templates/GroupBetsActive.html"
class GroupBetsCompletedView(TemplateView):
    template_name = "main_templates/GroupBetsCompleted.html"
class GroupBetsCreateView(TemplateView):
    template_name = "main_templates/GroupBetsCreate.html"
class GroupBetView(TemplateView):
    template_name = "main_templates/GroupBet.html"
class GroupBetAddView(TemplateView):
    template_name = "main_templates/GroupBetAdd.html"

class TestsView(TemplateView):
    template_name = "main_templates/Tests.html"