from django.test import TestCase


from cookbook.models import CookTime
from cookbook.test.mock.mock_data import ReadData


class CooktimeTest(TestCase):

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
    
    def test_cooktime_amount(self):
        """
        Test amount of Cooktime tags
        """
        self.assertEqual(6,CookTime.objects.count())
    
    def test_cooktime_30min(self):
        """
        Test filter 30-min tag 
        """
        self.assertEqual("30 min",CookTime.objects.filter(cooking_time="30 min"))

    def test_cooktime_morethan2hr(self):
        """
        Test filter more than 2 hr tag
        """
        self.assertEqual("30 min",CookTime.objects.filter(cooking_time="2 hr"))
    
    def test_cooktime_2hr(self):
        """
        Test filter 2 hr tag
        """
        self.assertEqual("2 hr",CookTime.objects.filter(cooking_time="2 hr"))

    def test_cooktime_1hr30min(self):
        """
        Test filter 1hr30min tag
        """
        self.assertEqual("1 hr 30 min",CookTime.objects.filter(cooking_time="1 hr 30 min"))
    
    def test_cooktime_1hr(self):
        """
        Test filter 1hr tag
        """
        self.assertEqual("1 hr",CookTime.objects.filter(cooking_time="1 hr"))
    
    def test_cooktime_15min(self):
        """
        Test filter 15 min tag
        """
        self.assertEqual("15 min",CookTime.objects.filter(cooking_time="15 min"))

    

