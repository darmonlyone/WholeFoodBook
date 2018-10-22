from django.urls import path

from . import views

app_name = 'cookbook'
urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('menu/', views.menu, name='menu'),
]
