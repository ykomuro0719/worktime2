from django.shortcuts import render
from .forms import CustomUserCreationForm,CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.http import Http404, HttpResponseRedirect,JsonResponse
from django.contrib.auth.views import LoginView,LogoutView
from .forms import CustomAuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'register/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register/user_new.html'
    success_url = '/'

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'register/profile.html'
    success_url = reverse_lazy('profile')

    def form_invalid(self, form):
        response = super(CustomPasswordChangeView,self).form_invalid(form)
        result_set = form.errors
        result_set['result'] = False
        return JsonResponse(result_set)

    def form_valid(self, form):
        response = super(CustomPasswordChangeView,self).form_valid(form)
        result_set = {'result':True,'msg':'更新しました'}
        return JsonResponse(result_set)