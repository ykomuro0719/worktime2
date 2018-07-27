from django.urls import path,re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    re_path(r'login/$', auth_views.login,{'template_name': 'register/login.html'},name='login'),
    re_path(r'logout/$', auth_views.logout, name='logout'),
    re_path(r'new/$', views.new, name='new'),
    re_path(r'create/$', views.create, name='create'),
    #re_path(r'^admin/', admin.site.urls),
]