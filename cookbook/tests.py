from django.test import TestCase

# from cookbook.models import CookTime, Equipment, Allergies, Category, Ingredient, Recipe
#
#
# class ModelTest(TestCase):
#
#     def __int__(self):
#         """
#         Initialize all model class
#         """
#         self.cooking_time = CookTime().objects.all()
#         self.cooking_equipment = Equipment().objects.all()
#         self.food_allergis = Allergies.objects.all()
#         self.food_category = Category().objects.all()
#         self.recipe = Recipe.objects.all()
#
#     def test_model_not_be_none(self):
#         """
#         Test model call should not be none.
#         """
#         self.assertIsNotNone(self.cooking_time)
#         self.assertIsNotNone(self.cooking_equipment)
#         self.assertIsNotNone(self.food_allergis)
#         self.assertIsNotNone(self.food_category)
#         self.assertIsNotNone(self.recipe)
#
#     def test_get_cooking_time(self):
#         """
#         Test time tags of recipe can tag in.
#         :return none
#         """
#         cooking_time = CookTime().objects.all()
#         self.assertEqual()
