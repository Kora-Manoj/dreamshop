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

from django.views.generic import FormView
from django.contrib.auth.models import User
from .forms import VendorRegistrationForm
from .models import UserProfile

class VendorRegisterView(FormView):
    template_name = 'users/vendor_register.html'
    form_class = VendorRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        UserProfile.objects.create(user=user, is_vendor=True)
        return super().form_valid(form)
