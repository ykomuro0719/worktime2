from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.views import LoginView,LogoutView
from .forms import CustomAuthenticationForm

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'register/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'register/logout.html'

class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register/user_new.html'
    success_url = '/'
