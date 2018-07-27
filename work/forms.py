from .models import Task,Level1,Level2,Level3
from django import forms
from django.contrib.auth.forms import UserCreationForm

 
class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['level1','level2','level3','day','time']
    widgets = {'day': forms.HiddenInput()}

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['day'].widget.attrs.update({'class':'form-control'})
    self.fields['time'].widget.attrs.update({'class':'form-control'})
    self.fields['level1'].widget.attrs.update({'class':'form-control'})
    self.fields['level2'].widget.attrs.update({'class':'form-control'})
    self.fields['level3'].widget.attrs.update({'class':'form-control'})
        
class CustomUserCreationForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({'class':'form-control'})
    self.fields['password1'].widget.attrs.update({'class':'form-control'})
    self.fields['password2'].widget.attrs.update({'class':'form-control'})
    

  