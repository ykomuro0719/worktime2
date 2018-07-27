from .models import Task,Level1,Level2,Level3
from django import forms

 
class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['level1','level2','level3','day','time']

  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['day'].widget.attrs.update({'class':'form-control'})
        self.fields['time'].widget.attrs.update({'class':'form-control'})
        self.fields['level1'].widget.attrs.update({'class':'form-control'})
        self.fields['level2'].widget.attrs.update({'class':'form-control'})
        self.fields['level3'].widget.attrs.update({'class':'form-control'})
