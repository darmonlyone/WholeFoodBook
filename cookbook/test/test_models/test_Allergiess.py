from django.test import TestCase


from cookbook.models import Allergies
from cookbook.test.mock.mock_data import ReadData


class AllergiesTest(TestCase):
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
    
    def test_allergies_amount(self):
        """
        Test amount of allergies
        """
        self.assertEqual(6,Allergies.objects.count())
    
    def test_allergy_egg(self):
        """
        Test filter tag egg
        """
        self.assertEqual("egg",Allergies.objects.filter(allergies_ingredient="egg"))

    def test_allergy_shrimp(self):
        """
        Test filter tag shrimp
        """
        self.assertEqual("shrimp",Allergies.objects.filter(allergies_ingredient="shrimp"))
    
    def test_allergy_soy(self):
        """
        Test filter tag soy
        """
        self.assertEqual("soy",Allergies.objects.filter(allergies_ingredient="soy"))

    def test_allergy_milk(self):
        """
        Test filter tag milk
        """
        self.assertEqual("milk",Allergies.objects.filter(allergies_ingredient="milk"))
    
    def test_allergy_shellfish(self):
        """
        Test filter tag shellfish
        """
        self.assertEqual("shellfish",Allergies.objects.filter(allergies_ingredient="shellfish"))
    
    def test_allergy_nuts(self):
        """
        Test filter tag nuts
        """
        self.assertEqual("nuts",Allergies.objects.filter(allergies_ingredient="nuts"))
    

