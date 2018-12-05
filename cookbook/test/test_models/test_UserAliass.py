from django.test import TestCase


from cookbook.models import *
from cookbook.test.mock.mock_data import ReadData


class UserTest(TestCase):
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
            self.assertEqual(recipe_from_author[i].recipe_name,recipe_from_alias[i].recipe_name)

    def test_alias_username(self):
        """
        Test Username has this Aliasname
        """
        tempAlias = UserAlias.objects.filter(user_username="Wanny")
        recipe_from_alias = []
        for i in tempAlias:
            recipe_from_alias.append(Recipe.objects.get(recipe_chef=i.recipe_chef))
        
        self.assertContains("Wan",recipe_from_alias[0].recipe_chef)
        tempAlias = []
        tempAlias = UserAlias.objects.filter(user_username="Noning")
        recipe_from_alias = []
        for i in tempAlias:
            recipe_from_alias.append(Recipe.objects.get(recipe_chef=i.recipe_chef))
        
        self.assertContains("Amy Finn",recipe_from_alias[0].recipe_chef)

    def test_author_recipename(self):
        tempUser = AuthorUser.objects.filter(user_username="Kung")
        recipe = [] 
        for i in tempUser:
            recipe.append(i.recipe_name)
        self.assertContains("Green Split Pea Soup",recipe)
        self.assertContains("Honey Garlic Salmon",recipe)
        self.assertContains("Honey Garlic Butternut Squash",recipe)

    
            