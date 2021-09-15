from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

#General views
class HomeView(TemplateView):
	template_name = "page/Home.html"
class AboutView(TemplateView):
	template_name = "page/About.html"
class TeamView(TemplateView):
	template_name = "page/Team.html"
class TermsAndConditionsView(TemplateView):
	template_name = "page/TermsAndConditions.html"  
class PrivacyPolicyView(TemplateView):
	template_name = "page/PrivacyPolicy.html"
 #Account pages views
class AccountView(TemplateView):
	template_name = "page/Account.html"
class AccountGroupsView(TemplateView):
	template_name = "page/AccountGroups.html"
class AccountSettingsView(TemplateView):
	template_name = "page/AccountSettings.html"

#Group pages views
class GroupView(TemplateView):
	template_name = "page/Group.html"
class GroupMembersView(TemplateView):
	template_name = "page/GroupMembers.html"
class GroupMembersAddView(TemplateView):
	template_name = "page/GroupMembersAdd.html"
class GroupBetsView(TemplateView):
	template_name = "page/GroupBets.html"
class GroupBetsActiveView(TemplateView):
	template_name = "page/GroupBetsActive.html"
class GroupBetsCompletedView(TemplateView):
	template_name = "page/GroupBetsCompleted.html"
class GroupBetsCreateView(TemplateView):
	template_name = "page/GroupBetsCreate.html"
class GroupBetView(TemplateView):
	template_name = "page/GroupBet.html"
class GroupBetAddView(TemplateView):
	template_name = "page/GroupBetAdd.html"

#Account pages views
class ExampleView:
	def component(request,componentName):
		return render(request,'page/example/component/'+componentName+'Page.html',{
			'title':componentName,
			'availableComponents':[
				'TextInput',
				'TextareaInput',
				'AnchorButton',
				'ExpandableContainer',
				'JsButton',
				'SubmitButton'
			]
		})
