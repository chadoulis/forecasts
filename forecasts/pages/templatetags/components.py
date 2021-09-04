from django_component import Library,Component
register=Library()


@register.component
class SimpleButton(Component):template='component/io/SimpleButton.html'

@register.component
class RoundBottomBorder(Component):template='component/decoration/RoundBottomBorder.html'

@register.component
class SimpleContainer(Component):template='component/containers/SimpleContainer.html'

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
class SimpleLayout(Component):template='layout/SimpleLayout.html'

@register.component
class RootLayout(Component):template='layout/RootLayout.html'