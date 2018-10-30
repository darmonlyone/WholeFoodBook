import tempfile
from django.core.files.images import ImageFile
from django.test import TestCase

from cookbook.models import CookTime, Equipment, Allergies, Category, Ingredient, Recipe


def get_test_image_file():
    file = tempfile.NamedTemporaryFile(suffix='.jpg')
    return ImageFile(file, name=file.name)


class ModelTest(TestCase):

    def setUp(self):
        """
        Set up database for testing.
        """
        CookTime.objects.create(cooking_time="10 Min")
        CookTime.objects.create(cooking_time="30 Min")
        CookTime.objects.create(cooking_time="1 Hours")
        Equipment.objects.create(equipment_required="mixer")
        Equipment.objects.create(equipment_required="blender")
        Allergies.objects.create(allergies_ingredient="egg")
        Allergies.objects.create(allergies_ingredient="milk")
        Allergies.objects.create(allergies_ingredient="soy")
        Category.objects.create(food_category="Main Course")
        mock_image = get_test_image_file()
        self.recipe = Recipe(recipe_chef="Darm", recipe_name="Fire egg", recipe_info="This is super egg of the years",
                             recipe_time=60, recipe_equipment="oven", recipe_fat=200,
                             recipe_ingredient="10g:Sugar||100%:love",
                             recipe_method="Put you egg in mixer||Take it off and fire with air",
                             recipe_image_1=mock_image)
        Recipe.objects.create(recipe_chef="Wanny", recipe_name="Super Chicken",
                              recipe_info="This checken come form real word that you will never know",
                              recipe_time=100, recipe_equipment="Fire", recipe_fat=1000,
                              recipe_ingredient="10000kg:Nothing",
                              recipe_method="Do nothing||Finished",
                              recipe_image_1='')

    def test_amount_cooking_time_tags(self):
        """
        Test amount of time tags of recipe can tag in.
        """
        self.assertEqual(CookTime.objects.count(), 3)

    def test_amount_equipment_tags(self):
        """
        Test amount of equipment tags of recipe can tag in.
        """
        self.assertEqual(Equipment.objects.count(), 2)

    def test_amount_allergies_tags(self):
        """
        Test amount of allergies tags of recipe can tag in.
        """
        self.assertEqual(Allergies.objects.count(), 3)

    def test_amount_category_tags(self):
        """
        Test amount of category tags of recipe can tag in.
        """
        self.assertEqual(Category.objects.count(), 1)

    def test_get_first_cooking_time_tags(self):
        """
        Test first time tags.
        """
        self.assertEqual(str(CookTime.objects.first()), "10 Min")

    def test_get_first_equipment_tags(self):
        """
        Test first equipment tags.
        """
        self.assertEqual(str(Equipment.objects.first()), "mixer")

    def test_get_first_allergies_tags(self):
        """
        Test first allergies tags.
        """
        self.assertEqual(str(Allergies.objects.first()), "egg")

    def test_get_first_category_tags(self):
        """
        Test first time tags.
        """
        self.assertEqual(str(Category.objects.first()), "Main Course")

    def test_get_recipe_chef(self):
        """
        Test check recipe chef.
        """
        self.assertEqual(self.recipe.get_recipe_chef(), "Darm")

    def test_get_recipe_name(self):
        """
        Test check recipe name.
        """
        self.assertEqual(self.recipe.get_recipe_name(), "Fire egg")

    def test_get_recipe_info(self):
        """
        Test check recipe detail.
        """
        self.assertEqual(self.recipe.get_recipe_info(), "This is super egg of the years")

    def test_get_recipe_time(self):
        """
        Test check recipe time.
        """
        self.assertEqual(self.recipe.get_recipe_time(), 60)

    def test_get_recipe_equipment(self):
        """
        Test check recipe equipment require.
        """
        self.assertTrue(self.recipe.get_recipe_equipment().isupper())
        self.assertEqual(self.recipe.get_recipe_equipment(), "OVEN")

    def test_get_recipe_fat(self):
        """
        Test check food fat of the recipe.
        """
        self.assertEqual(self.recipe.get_recipe_fat(), 200)

    def test_get_recipe_method_list(self):
        """
        Test check food fat of the recipe.
        """
        method_list = self.recipe.get_recipe_method_list()
        for i in method_list:
            self.assertTrue(i)
        self.assertEqual(method_list[0], "Put you egg in mixer")
        self.assertEqual(method_list[1], "Take it off and fire with air")

    def test_get_recipe_image_not_be_none(self):
        """
        Test recipe image not be none.
        """
        self.assertIsNotNone(self.recipe.get_recipe_image_1())

    def test_get_recipe_ingredient(self):
        """
        Test get recipe ingredient with Ingredient class.
        """
        ingredients = self.recipe.get_recipe_ingredient()
        for i in ingredients:
            self.assertTrue(i.get_detail())
            self.assertTrue(i.get_amount())
        self.assertEqual(ingredients[0].get_amount(), "10g")
        self.assertEqual(ingredients[0].get_detail(), "Sugar")
        self.assertEqual(ingredients[1].get_amount(), "100%")
        self.assertEqual(ingredients[1].get_detail(), "love")

    def test_recipe_filter(self):
        """
        Test recipe filter from model.
        """
        self.assertTrue(Recipe.objects.filter(recipe_chef="Wanny", recipe_fat=1000))
        self.assertFalse(Recipe.objects.filter(recipe_time=99, recipe_name="Tello"))
