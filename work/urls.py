from django.urls import path,re_path,include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, permission_required
from . import views


urlpatterns = [
    path('', login_required(views.IndexView.as_view()),name='index'),
    path('<int:year>/<int:month>/<int:day>',login_required(views.TaskCreateView.as_view()),name='day-page'),
    path('fetch_child_select', views.fetch_child_select, name="fetch_child_select"),
    path('task/delete',views.delete_task, name="delete_task"),
    path('fetch_registered_task',views.fetch_registered_task, name="fetch_registered_task"),
]