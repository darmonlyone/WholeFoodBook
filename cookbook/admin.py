from django.contrib import admin
from .models import Recipe, CookTime, Category, Allergies, Equipment


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'recipe_chef')
    list_filter = ['category_tags', 'time_tags', 'equipment_tags', 'allergies_tags']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
admin.site.register(CookTime)
admin.site.register(Equipment)
admin.site.register(Allergies)
