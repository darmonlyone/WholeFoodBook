from django.urls import path

from . import views

app_name = 'cookbook'
urlpatterns = [
    path('', views.welcome, name='welcome'),
]
