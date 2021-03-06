from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
        
class CustomUserCreationForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({'class':'form-control form-control-lg'})
    self.fields['password1'].widget.attrs.update({'class':'form-control form-control-lg'})
    self.fields['password2'].widget.attrs.update({'class':'form-control form-control-lg'})
    
class CustomAuthenticationForm(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({'class':'form-control form-control-lg'})
    self.fields['password'].widget.attrs.update({'class':'form-control form-control-lg'})

class CustomPasswordChangeForm(PasswordChangeForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['old_password'].widget.attrs.update({'class':'form-control form-control-lg'})
    self.fields['new_password1'].widget.attrs.update({'class':'form-control form-control-lg'})
    self.fields['new_password2'].widget.attrs.update({'class':'form-control form-control-lg'})