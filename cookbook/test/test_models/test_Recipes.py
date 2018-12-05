from django.test import TestCase


from cookbook.models import *
from cookbook.test.mock.mock_data import ReadData


class RecipesTest(TestCase):
    def setUp(self):
        """
        Set up database for testing.
        """
        self.set_data()

    @staticmethod
    def set_data():
        read = ReadData()
        for time in read.time_tags:
            CookTime.objects.create(cooking_time=time)
        for equipment in read.equipment_tags:
            Equipment.objects.create(equipment_required=equipment)
        for allergies in read.allergies_tags:
            Allergies.objects.create(allergies_ingredient=allergies)
        for category in read.category_tags:
            Category.objects.create(food_category=category)
        for author in read.author_user:
            AuthorUser.objects.create(user_username=author[0], recipe_name=author[1])
        for alias in read.user_alias:
            UserAlias.objects.create(user_username=alias[0], alias_name=alias[1])
        for recipe in read.recipe_list:
            Recipe.objects.create(recipe_chef=recipe[0], recipe_name=recipe[1], recipe_info=recipe[2],
                                  recipe_time=recipe[3], recipe_equipment=recipe[4], recipe_fat=recipe[5],
                                  recipe_ingredient=recipe[6], recipe_method=recipe[7])

    def test_recipe_chef(self):
        """
        Test get recipe's chef name
        """
        recipe = Recipe.objects.get(recipe_name="Chicken Breast")
        self.assertEqual("Wan",recipe.recipe_chef)
        recipe = Recipe.objects.get(recipe_chef="Amy Finn")
        self.assertEqual("Chicken Chickpea Stew",recipe.recipe_name)
    
    def test_recipe_ingredient(self):
        """
        Test get recipe's ingredient
        """
        recipe = Recipe.objects.get(recipe_name="Chicken Breast")
        self.assertContains("kipfler potatoes",recipe.recipe_ingredient)
        self.assertContains("olive oil",recipe.recipe.recipe_ingredient)
        self.assertContains("macadamia nuts",recipe.recipe_ingredient)
    
    def test_recipe_method(self):
        """
        Test get recipe's method
        """
        recipe = Recipe.objects.get(recipe_name="Strawberry Yogurt")
        self.assertContains("Place strawberries in a glass or serving dish and cut using kitchen shears until mushy. You can also use a food processor if making multiples (don’t over process into complete mush) or mash berries with a muddler.",recipe.recipe_method)
        self.assertContains("Add maple syrup and mix well. Add Greek yogurt and stir gently to combine.",recipe.recipe_method)

    def test_recipe_info(self):
        """
        Test get recipe's info
        """
        recipe = Recipe.objects.get(recipe_name="Healthy Chicken Broccoli")
        self.assertContains("Almost One Pot Healthy Chicken Broccoli Casserole Recipe that is saucy with firm pasta and crunchy broccoli.",recipe.recipe_info)

        
