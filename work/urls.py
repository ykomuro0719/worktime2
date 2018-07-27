from django.urls import path,re_path,include
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:year>/<int:month>/<int:day>',views.TaskCreateView.as_view(),name='day-page')
]