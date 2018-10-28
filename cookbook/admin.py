from django.contrib import admin
from .models import Recipe, CookTime, Allergies, Equipment


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'recipe_chef')
    list_filter = ['time_tags']


admin.site.register(CookTime)
admin.site.register(Equipment)
admin.site.register(Allergies)
admin.site.register(Recipe, RecipeAdmin)

