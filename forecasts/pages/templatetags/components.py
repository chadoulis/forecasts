from django_component import Library,Component
register=Library()


@register.component
class SimpleContainer(Component):template='component/container/SimpleContainer.html'

@register.component
class ExpandableContainer(Component):template='component/container/ExpandableContainer.html'

@register.component
class SimpleContainerLayout(Component):template='component/container/_layout/SimpleContainerLayout.html'

@register.component
class SimpleContainerWithButtonLayout(Component):template='component/container/_layout/SimpleContainerWithButtonLayout.html'

@register.component
class RoundBottomBorder(Component):template='component/decoration/RoundBottomBorder.html'

@register.component
class ErrorMessage(Component):template='component/message/ErrorMessage.html'

@register.component
class SimpleLayout(Component):template='component/layout/SimpleLayout.html'

@register.component
class RootLayout(Component):template='component/layout/RootLayout.html'

@register.component
class SubmitButton(Component):template='component/button/SubmitButton.html'

@register.component
class AnchorButton(Component):template='component/button/AnchorButton.html'

@register.component
class OnClickButton(Component):template='component/button/OnClickButton.html'

@register.component
class SimpleButtonLayout(Component):template='component/button/_layout/SimpleButtonLayout.html'

@register.component
class TermsAndConditions(Component):template='page/TermsAndConditions.html'

@register.component
class GroupBet(Component):template='page/GroupBet.html'

@register.component
class AccountSettings(Component):template='page/AccountSettings.html'

@register.component
class ConfirmAccount(Component):template='page/ConfirmAccount.html'

@register.component
class PrivacyPolicy(Component):template='page/PrivacyPolicy.html'

@register.component
class ResetPassword(Component):template='page/ResetPassword.html'

@register.component
class GroupBetAdd(Component):template='page/GroupBetAdd.html'

@register.component
class GroupBets(Component):template='page/GroupBets.html'

@register.component
class Login(Component):template='page/Login.html'

@register.component
class GroupBetsCreate(Component):template='page/GroupBetsCreate.html'

@register.component
class GroupMembersAdd(Component):template='page/GroupMembersAdd.html'

@register.component
class GroupMembers(Component):template='page/GroupMembers.html'

@register.component
class GroupBetsCompleted(Component):template='page/GroupBetsCompleted.html'

@register.component
class Register(Component):template='page/Register.html'

@register.component
class ForgotPassword(Component):template='page/ForgotPassword.html'

@register.component
class About(Component):template='page/About.html'

@register.component
class GroupBetsActive(Component):template='page/GroupBetsActive.html'

@register.component
class Group(Component):template='page/Group.html'

@register.component
class AccountGroups(Component):template='page/AccountGroups.html'

@register.component
class Account(Component):template='page/Account.html'

@register.component
class Team(Component):template='page/Team.html'

@register.component
class Home(Component):template='page/Home.html'

@register.component
class TermsAndConditions(Component):template='main_templates/TermsAndConditions.html'

@register.component
class GroupBet(Component):template='main_templates/GroupBet.html'

@register.component
class AccountSettings(Component):template='main_templates/AccountSettings.html'

@register.component
class ConfirmAccount(Component):template='main_templates/ConfirmAccount.html'

@register.component
class PrivacyPolicy(Component):template='main_templates/PrivacyPolicy.html'

@register.component
class ResetPassword(Component):template='main_templates/ResetPassword.html'

@register.component
class GroupBetAdd(Component):template='main_templates/GroupBetAdd.html'

@register.component
class GroupBets(Component):template='main_templates/GroupBets.html'

@register.component
class Login(Component):template='main_templates/Login.html'

@register.component
class GroupBetsCreate(Component):template='main_templates/GroupBetsCreate.html'

@register.component
class GroupMembersAdd(Component):template='main_templates/GroupMembersAdd.html'

@register.component
class GroupMembers(Component):template='main_templates/GroupMembers.html'

@register.component
class GroupBetsCompleted(Component):template='main_templates/GroupBetsCompleted.html'

@register.component
class Register(Component):template='main_templates/Register.html'

@register.component
class ForgotPassword(Component):template='main_templates/ForgotPassword.html'

@register.component
class GroupBetsActive(Component):template='main_templates/GroupBetsActive.html'

@register.component
class Group(Component):template='main_templates/Group.html'

@register.component
class AccountGroups(Component):template='main_templates/AccountGroups.html'

@register.component
class Account(Component):template='main_templates/Account.html'

@register.component
class Team(Component):template='main_templates/Team.html'

idIndex=-1
onceBuffer={}
@register.simple_tag
def id():
	global idIndex
	idIndex+=1
	return idIndex
@register.simple_tag
def once(comp):
	global onceBuffer;
	try:
		onceBuffer[comp]
		return False
	except:
		onceBuffer[comp]=True
		return True
@register.simple_tag
def reset():
	global idIndex,onceBuffer
	idIndex=-1
	onceBuffer={}
	return''
