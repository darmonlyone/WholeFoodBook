from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'cookbook'
urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    # path('database/', views.fake_put_db),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
