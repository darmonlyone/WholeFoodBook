from django.contrib import admin
from .models import Recipe


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'recipe_chef')


admin.site.register(Recipe, AuthorAdmin)
