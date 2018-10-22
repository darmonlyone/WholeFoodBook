from django.db import models


class Recipe(models.Model):
    user = models.CharField(max_length=30)
    recipe_name = models.CharField(max_length=30)
    recipe_info = models.TextField()
    recipe_time = models.IntegerField(null=True)
    recipe_type = models.CharField(max_length=15)
    recipe_fat = models.IntegerField(null=True)
    recipe_ingredient = models.TextField()
    recipe_method = models.TextField()

    def _str__(self):
        return f"{self.user}: {self.recipe_name}"

    def get_user(self):
        return self.user

    def get_recipe_name(self):
        return self.recipe_name

    def get_recipe_info(self):
        return self.recipe_info

    def get_recipe_time(self):
        return self.recipe_time

    def get_recipe_type(self):
        return self.recipe_type

    def get_recipe_fat(self):
        return self.recipe_fat

    def get_recipe_ingredient(self):
        return self.recipe_ingredient

    def get_recipe_method(self):
        return self.recipe_method
