from django.db import models


class Recipe(models.Model):
    recipe_chef = models.CharField(max_length=30)
    recipe_name = models.CharField(max_length=30)
    recipe_info = models.TextField()
    recipe_time = models.IntegerField(null=True)
    recipe_type = models.CharField(max_length=15)
    recipe_fat = models.IntegerField(null=True)
    recipe_ingredient = models.TextField()
    recipe_method = models.TextField()

    def _str__(self):
        return f"Chef: {self.recipe_chef}: {self.recipe_name}"

    def get_recipe_chef(self):
        return self.recipe_chef

    def get_recipe_name(self):
        return self.recipe_name

    def get_recipe_info(self):
        return self.recipe_info

    def get_recipe_time(self):
        return self.recipe_time

    def get_recipe_type(self):
        return self.recipe_type.upper()

    def get_recipe_fat(self):
        return self.recipe_fat

    def get_recipe_ingredient(self):
        ingredients = self.recipe_ingredient.split("||")
        ingredient = []
        for i in ingredients:
            splitter = i.split(":")
            ingredient.append(Ingredient(splitter[0], splitter[1]))
        return ingredient

    def get_recipe_method(self):
        return self.recipe_method

    def get_recipe_method_list(self):
        return self.recipe_method.split("||")

class Ingredient:

    def __init__(self, amount, detail):
        self.amount = amount
        self.detail = detail

    def get_detail(self):
        return self.detail

    def get_amount(self):
        return self.amount
