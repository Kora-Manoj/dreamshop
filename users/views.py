from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
