from django.test import TestCase


from cookbook.models import Equipment
from cookbook.test.mock.mock_data import ReadData


class EquipmentTest(TestCase):
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

    def test_equipment_amount(self):
        """
        Test amount of Equipment tags
        """
        self.assertEqual(4,Equipment.objects.count())
    
    def test_equipment_blender(self):
        """
        Test equipment blender filter
        """
        self.assertEqual("blender",Equipment.objects.filter(equipment_required="blender"))
    
    def test_equipment_mixer(self):
        """
        Test equipment mixer filter
        """
        self.assertEqual("mixer",Equipment.objects.filter(equipment_required="mixer"))

    def test_equipment_microwave(self):
        """
        Test equipment microwave filter
        """
        self.assertEqual("microwave",Equipment.objects.filter(equipment_required="microwave"))

    def test_equipment_oven(self):
        """
        Test equipment oven filter
        """
        self.assertEqual("oven",Equipment.objects.filter(equipment_required="oven"))
