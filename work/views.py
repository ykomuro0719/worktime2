from django.shortcuts import render
from .models import *
from .forms import TaskForm
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect,JsonResponse
import datetime

class IndexView(TemplateView):
  template_name = 'work/index.html'

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TaskCreateView(CreateView):
  template_name = 'work/detail.html'
  model = Task
  form_class = TaskForm
  success_url = reverse_lazy('index')

  def get_success_url(self):
    year,month,day = self.kwargs['year'],self.kwargs['month'],self.kwargs['day']
    self.success_url += f'{year}/{month}/{day}'
    return self.success_url

  def get_initial(self):
    super(TaskCreateView, self).get_initial()
    target = datetime.date(self.kwargs['year'],self.kwargs['month'],self.kwargs['day'])
    self.initial = {'day':target,'user':self.request.user.id}
    return self.initial

  def get_context_data(self,**kwargs):
    context = super(TaskCreateView, self).get_context_data(**kwargs)
    target = datetime.date(self.kwargs['year'],self.kwargs['month'],self.kwargs['day'])
    tasks = Task.objects.filter(day=target,user=self.request.user.id)
    data = {'tasks':tasks,'year':self.kwargs['year'],'month':self.kwargs['month'],'day':self.kwargs['day']}
    context.update(data)
    return context

  def post(self, request, *args, **kwargs):
    cp_request_post = request.POST.copy()
    cp_request_post['user'] = request.user.id
    self.request.POST = cp_request_post
    request.POST = cp_request_post
    return super(TaskCreateView, self).post(request, *args, **kwargs)

def fetch_child_select(request):
  try:
    num = int(request.GET.get('num'))
    level = request.GET.get('level')
    
    if level == 'level1':
      ids = [l2[0] for l2 in Level2.objects.filter(level1_id=num).values_list('id')]
    elif level == 'level2':
      ids = [l3[0] for l3 in Level3.objects.filter(level2_id=num).values_list('id')]
  except Exception:
    ids = []
  finally:
    result = {'ids':ids}
    return JsonResponse(result)