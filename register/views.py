from django.shortcuts import render
from .forms import CustomUserCreationForm,CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.http import Http404, HttpResponseRedirect,JsonResponse
from django.contrib.auth.views import LoginView,LogoutView
from .forms import CustomAuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Count
from work.models import Task,Level1,Level2,Level3
import datetime

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

def fetch_statistics(request):
    today = datetime.date.today()
    agg_start = today - datetime.timedelta(days=30)
    statistics_data = {}
    for i in range(1,4):
        exec('''\
l{0}_raw_data = Task.objects.filter(user=request.user.id,day__gte=agg_start,day__lte=today)\
.values('level{0}_id','level{0}__title').annotate(level{0}_nums = Count('level{0}_id'))\
.order_by('level{0}_nums').reverse()
l{0}_data = []
dt2 = dict()
for i,data in enumerate(l{0}_raw_data):
    if i < 5:
        dt = dict()
        dt['title'] = data['level{0}__title']
        dt['count'] = data['level{0}_nums']
        l{0}_data.append(dt)
    else:
        if i==5:
            dt2['title'] = 'other'
            dt2['count'] = 0
        dt2['count'] += data['level{0}_nums']
l{0}_data.append(dt2)
statistics_data['level{0}'] = l{0}_data
    '''.format(str(i)))
    return JsonResponse(statistics_data)