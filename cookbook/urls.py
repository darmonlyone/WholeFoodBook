from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'cookbook'
urlpatterns = [
    path('',views.ProfileViewTest.as_view(), name='popup'),
    # path('', views.WelcomeView.as_view(), name='welcome'),
    # path('recipe/<str:recipe_name>', views.MenuView.as_view(), name='recipe'),
    path ('profile/',views.ProfileView.as_view(), name='profile'),
    # # path('database/', views.fake_put_db),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
