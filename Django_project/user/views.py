from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView
from user.forms import CustomUserCreationForm


class UserRegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('user:login')

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