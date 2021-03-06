from django.test import TestCase

from cookbook.models import *
from cookbook.test.mock.mock_data import ReadData
from cookbook.models import *
from cookbook.test.mock import mock_data


class RecipesTest(TestCase):

    def test_recipe_chef(self):
        """
        Test get recipe's chef name
        """
        recipe = Recipe.objects.get(recipe_name="Chicken Breast")
        self.assertEqual("Wan", recipe.recipe_chef)
        recipe = Recipe.objects.get(recipe_chef="Amy Finn")
        self.assertEqual("Chicken Chickpea Stew", recipe.recipe_name)

    def test_recipe_ingredient(self):
        """
        Test get recipe's ingredient
        """
        recipe = Recipe.objects.get(recipe_name="Chicken Breast")
        self.assertIn("kipfler potatoes", recipe.recipe_ingredient)
        self.assertIn("olive oil", recipe.recipe_ingredient)
        self.assertIn("macadamia nuts", recipe.recipe_ingredient)

    def test_recipe_method(self):
        """
        Test get recipe's method
        """
        recipe = Recipe.objects.get(recipe_name="Strawberry Yogurt")
        self.assertIn(
            "Place strawberries in a glass or serving dish and cut using kitchen shears until mushy. You can also use a food processor if making multiples (don’t over process into complete mush) or mash berries with a muddler.",
            recipe.recipe_method)
        self.assertIn("Add maple syrup and mix well. Add Greek yogurt and stir gently to combine.",
                            recipe.recipe_method)

    def test_recipe_info(self):
        """
        Test get recipe's info
        """
        recipe = Recipe.objects.get(recipe_name="Healthy Chicken Broccoli")
        self.assertIn(
            "Almost One Pot Healthy Chicken Broccoli Casserole Recipe that is saucy with firm pasta "
            "and crunchy broccoli.", recipe.recipe_info)
