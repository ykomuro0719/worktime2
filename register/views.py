from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect

def new(request):
  form = CustomUserCreationForm()
  return render(request, 'register/user_new.html', {'form': form,})

def create(request):
  if request.method == 'POST':
      form = CustomUserCreationForm(request.POST)
      if form.is_valid():
          form.save()
          return HttpResponseRedirect('./login')
      return render(request, 'register/user_new.html', {'form': form,})
  else:
      raise Http404