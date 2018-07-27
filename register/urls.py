from django.urls import path,re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    re_path(r'login/$', views.CustomLoginView.as_view(),name='login'),
    re_path(r'logout/$', views.CustomLogoutView.as_view(), name='logout'),
    re_path(r'new/$', views.UserCreateView.as_view(), name='new'),
    #re_path(r'create/$', views.create, name='create'),
    re_path(r'^admin/', admin.site.urls),
]