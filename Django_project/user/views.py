from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, FormView
from user.forms import CustomUserCreationForm
from django.core.mail import send_mail


class UserRegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        self.send_verification_email(user)
        messages.success(self.request, 'Account created successfully, Check your email to activate your account.')
        return redirect('user:login')

    def send_verification_email(self, user):
        uid = user.pk
        token = default_token_generator.make_token(user)
        activation_link = self.request.build_absolute_uri(
            reverse('user:activate', kwargs={'uid': uid, 'token': token})
        )
        subject = "Activate Account"
        message = f'Hi {user.username}, Please click on the link to activate your account {activation_link}.'
        send_mail(subject, message, from_email='', recipient_list=[user.email])

    def form_invalid(self, form):
        messages.error(self.request, "Something is incorrect")
        return super().form_invalid(form)

def activate_account(request, uid, token):
    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return HttpResponse('User does not exist', status=404)

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Account activated successfully")
        return redirect('user:login')
    else:
        return HttpResponse('Token is invalid or expired')

class UserLoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('core:index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:index')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect(self.success_url)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('user:login')