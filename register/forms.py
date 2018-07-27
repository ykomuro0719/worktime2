from django import forms
from django.contrib.auth.forms import UserCreationForm
        
class CustomUserCreationForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({'class':'form-control'})
    self.fields['password1'].widget.attrs.update({'class':'form-control'})
    self.fields['password2'].widget.attrs.update({'class':'form-control'})
    

  