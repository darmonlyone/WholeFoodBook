from django.test import TestCase


from cookbook.models import Category
from cookbook.test.mock.mock_data import ReadData


class CategoriesTest(TestCase):
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
      
    def test_categories_amount(self):
        """
        Test amount of category tags
        """
        self.assertEqual(6,Category.objects.count())
    
    def test_categories_drink(self):
        """
        Test categories drink filter
        """
        self.assertEqual("drink",Category.objects.filter(food_category="drink"))
    
    def test_categories_dessert(self):
        """
        Test categories dessert filter
        """
        self.assertEqual("dessert",Category.objects.filter(food_category="dessert"))

    def test_categories_soup(self):
        """
        Test categories soup and stew filter
        """
        self.assertEqual("soup and stew",Category.objects.filter(food_category="soup and stew"))

    def test_categories_main(self):
        """
        Test categories main dish filter
        """
        self.assertEqual("main dish",Category.objects.filter(food_category="main dish"))

    def test_categories_salad(self):
        """
        Test categories salad filter
        """
        self.assertEqual("salad",Category.objects.filter(food_category="salad"))
    
    def test_categories_appetizer(self):
        """
        Test categories appetizer filter
        """"
        self.assertEqual("appetizer",Category.object.fliter(food_category="appetizer"))
