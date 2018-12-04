from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'cookbook'
urlpatterns = [
                  path('logout/', views.logout, name='logout'),
                  path('', views.WelcomeView.as_view(), name='welcome'),
                  path('add/recipe/', views.AddRecipeView.as_view(), name='addRecipe'),
                  path('add/recipe/confirm/', views.update_recipe, name='addRecipe_request'),
                  path('recipe/<str:recipe_name>', views.MenuView.as_view(), name='recipe'),
                  path('edit/recipe/<str:recipe_name>', views.EditRecipeView.as_view(), name='edit'),
                  path('delete/recipe/<str:recipe_name>', views.DeleteRecipeView.as_view(), name='delete_recipe'),
                  path('login/', views.LoginView.as_view(), name='login'),
                  path('index/', views.IndexView.as_view(), name='index'),
                  path('profile/', views.ProfileView.as_view(), name='profile'),
                  path('profile/update/alias', views.userAliasPost, name='updateAlias'),
                  path('search/', views.SearchView.as_view(), name='search'),
                  path('search/<str:recipe_search>', views.SearchView.as_view(), name='search'),
                  path('searcher', views.search, name='searcher'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)