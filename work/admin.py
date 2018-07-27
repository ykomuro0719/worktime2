from django.contrib import admin
from .models import Task,Level1,Level2,Level3

model_list = [Task,Level1,Level2,Level3]
for model in model_list:
  admin.site.register(model)
