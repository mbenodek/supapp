from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('tracker/', views.tracker, name='tracker'),
    path('life/', views.tracker, name='life'),

]