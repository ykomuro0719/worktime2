from django.urls import path,re_path,include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, permission_required
from . import views


urlpatterns = [
    path('', login_required(views.IndexView.as_view()),name='index'),
    path('<int:year>/<int:month>/<int:day>',login_required(views.TaskCreateView.as_view()),name='day-page'),
    path('fetch_child_select', views.fetch_child_select, name="fetch_child_select")
]