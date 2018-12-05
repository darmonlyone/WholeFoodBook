from django.test import TestCase

from cookbook.models import *


class UserTest(TestCase):

    def test_same_alias(self):
        """
        Test same recipe_chef from Author username and Useralias username
        """
        tempAuthor = AuthorUser.objects.filter(user_username="Darm")
        recipe_from_author = []
        for i in tempAuthor:
            recipe_from_author.append(Recipe.objects.get(recipe_name=i.recipe_name))

        tempUser = UserAlias.objects.filter(user_username="Darm")
        for i in range(len(tempUser)):
            self.assertEqual(recipe_from_author[i].recipe_chef, tempUser[i].alias_name)

    def test_same_recipe(self):
        """
        Test same recipe_name from author username and UserAlias aliasname
        """
        tempAuthor = AuthorUser.objects.filter(user_username="Beauty.B")
        recipe_from_author = []
        for i in tempAuthor:
            recipe_from_author.append(Recipe.objects.get(recipe_name=i.recipe_name))

        tempAlias = UserAlias.objects.filter(user_username="Olena")
        recipe_from_alias = []
        for i in tempAlias:
            recipe_from_alias.append(Recipe.objects.get(recipe_name=i.recipe_chef))

        for i in range(len(tempAlias)):
            self.assertEqual(recipe_from_author[i].recipe_name, recipe_from_alias[i].recipe_name)

    def test_alias_username(self):
        """
        Test Username has this Aliasname
        """
        tempAlias = UserAlias.objects.filter(user_username="Wanny")
        recipe_from_alias = []
        for i in tempAlias:
            recipe_from_alias.append(Recipe.objects.get(recipe_chef=i.alias_name))

        self.assertIn("Wan", recipe_from_alias[0].recipe_chef)
        tempAlias = []
        tempAlias = UserAlias.objects.filter(user_username="Noning")
        recipe_from_alias = []
        for i in tempAlias:
            recipe_from_alias.append(Recipe.objects.get(recipe_chef=i.alias_name))
        self.assertIn("Amy Finn", recipe_from_alias[0].recipe_chef)

    def test_author_recipename(self):
        tempUser = AuthorUser.objects.filter(user_username="Kung")
        recipe = []
        for i in tempUser:
            recipe.append(i.recipe_name)
        self.assertIn( "Green Split Pea Soup", recipe )
        self.assertIn("Honey Garlic Salmon", recipe)
        self.assertIn("Honey Garlic Butternut Squash",recipe)
