from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'cookbook'
urlpatterns = [
                  path('logout/', views.logout, name='logout'),
                  path('', views.WelcomeView.as_view(), name='welcome'),
                  path('add/recipe/', views.AddRecipeView.as_view(), name='addRecipe'),
                  path('recipe/<str:recipe_name>', views.MenuView.as_view(), name='recipe'),
                  path('recipe/edit/<str:recipe_name>', views.MenuView.as_view(), name='edit'),
                  path('recipe/delete/<str:recipe_name>', views.DeleteRecipeView.as_view(), name='delete_recipe'),
                  path('login/', views.LoginView.as_view(), name='login'),
                  path('index/', views.IndexView.as_view(), name='index'),
                  path('profile/', views.ProfileView.as_view(), name='profile'),
                  path('profile/update/alias', views.userAliasPost, name='updateAlias'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)