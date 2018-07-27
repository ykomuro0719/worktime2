from django.shortcuts import render
from .models import *
from .forms import TaskForm
from django.views.generic.base import TemplateView
from django.views.generic import CreateView

class IndexView(TemplateView):
  template_name = 'work/index.html'

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TaskCreateView(CreateView):
  template_name = 'work/detail.html'
  model = Task
  form_class = TaskForm
  success_url = "/"
  
  def get_context_data(self, year=None,month=None,day=None,**kwargs):
    context = super(TaskCreateView, self).get_context_data(**kwargs)
    return context
