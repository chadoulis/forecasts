from django.contrib.auth.views import LoginView, PasswordResetView
from django.shortcuts import resolve_url, get_object_or_404
from django.views.generic import TemplateView

from forecasts.users.models import CustomUser


class CustomLoginView(LoginView):
    template_name = "page/Login.html"


class RegisterView(LoginView):
    template_name = "page/Register.html"


class ForgotPasswordView(TemplateView):
    template_name = "page/ForgotPassword.html"


class CustomPasswordResetView(PasswordResetView):
    template_name = "page/ResetPassword.html"


class ConfirmAccountView(TemplateView):
    template_name = "page/ConfirmAccount.html"


class ProfileView(TemplateView):
    template_name = "page/Profile.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        username = kwargs.get('username')
        if username:
            user = get_object_or_404(CustomUser, username=username)

        if request.user.is_authenticated:
            if username == request.user.username:
                context['view_settings'] = True


        return self.render_to_response(context)