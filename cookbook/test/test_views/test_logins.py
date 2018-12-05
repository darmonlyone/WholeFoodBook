from django.test import TestCase
from cookbook.models import Recipe

class TestAddRecipe(TestCase):
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


    def test_login_response(self):
        """
        Test check that index page is work.

        """
        response = self.client.get(reverse('cookbook:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_response(self):
        """
        Test check contain Sign in.
        
        """
        response = self.client.get(reverse('cookbook:login'))
        self.assertContains(response,"Sign in")