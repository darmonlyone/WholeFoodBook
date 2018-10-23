from django.urls import path

from . import views

app_name = 'cookbook'
urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    # path('database/', views.fake_put_db),
]
