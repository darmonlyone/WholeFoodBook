from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'cookbook'
urlpatterns = [
                  path('home/', views.home, name='home'),
                  path('', views.WelcomeView.as_view(), name='welcome'),
                  path('recipe/<str:recipe_name>', views.MenuView.as_view(), name='recipe'),
                  path('login/', views.LoginView.as_view(), name='login'),
                  path('index/', views.IndexView.as_view(), name='index'),
                  path('profile/', views.ProfileView.as_view(), name='profile'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
