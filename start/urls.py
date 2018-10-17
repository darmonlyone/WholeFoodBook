from django.urls import path

from . import views

app_name = 'start'
urlpatterns = [
    path('', views.index, name='index'),
    path('welcome/', views.welcome, name='welcome'),
]
