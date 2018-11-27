from django.contrib import admin
from .models import *


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'recipe_chef')
    list_filter = ['category_tags', 'time_tags', 'equipment_tags', 'allergies_tags']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'user_username')
    list_filter = ['user_username']


class AliasAdmin(admin.ModelAdmin):
    list_display = ('alias_name', 'user_username')
    list_filter = ['user_username']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
admin.site.register(CookTime)
admin.site.register(Equipment)
admin.site.register(Allergies)
admin.site.register(AuthorUser, AuthorAdmin)
admin.site.register(UserAlias, AliasAdmin)
