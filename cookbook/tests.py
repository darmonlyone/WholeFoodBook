from django.test import TestCase
from django.urls import reverse

from cookbook.models import CookTime, Equipment, Allergies, Category, Recipe


class ViewTest(TestCase):

    def test_no_recipe(self):
        """
        If no recipe exist, an appropriate message is displayed.
        """
        # pass
        response = self.client.get(reverse('cookbook:recipe', args=['darm']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This Recipe are not available.")
        self.assertQuerysetEqual(response.context['recipe_enable'], [])

    def test_welcome_page(self):
        """
        Test status code form opening welcome page.
        """
        response = self.client.get(reverse('cookbook:welcome'))
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        """
        Test status code form opening login page.
        """
        response = self.client.get(reverse('cookbook:login'))
        self.assertEqual(response.status_code, 200)

    def test_index_page(self):
        """
        Test status code from opening index page.
        """
        # pass
        response = self.client.get(reverse('cookbook:index'))
        self.assertEquals(response.status_code, 200)


class ModelTest(TestCase):

    def setUp(self):
        """
        Set up database for testing.
        """
        CookTime.objects.create(cooking_time="10 Mins")
        CookTime.objects.create(cooking_time="30 Mins")
        CookTime.objects.create(cooking_time="1 Hour")
        Equipment.objects.create(equipment_required="mixer")
        Equipment.objects.create(equipment_required="blender")
        Allergies.objects.create(allergies_ingredient="egg")
        Allergies.objects.create(allergies_ingredient="milk")
        Allergies.objects.create(allergies_ingredient="soy")
        Category.objects.create(food_category="Main Course")
        Recipe.objects.create(recipe_chef="Darm", recipe_name="Fire egg",
                              recipe_info="This is super egg of the years",
                              recipe_time=60, recipe_equipment="oven", recipe_fat=200,
                              recipe_ingredient="10g:Sugar||100%:love",
                              recipe_method="Put you egg in mixer||Take it off and fire with air",
                              recipe_image_1='')
        Recipe.objects.create(recipe_chef="Wanny", recipe_name="Super Chicken",
                              recipe_info="This checken come form real word that you will never know",
                              recipe_time=100, recipe_equipment="Fire", recipe_fat=1000,
                              recipe_ingredient="10000kg:Nothing",
                              recipe_method="Do nothing||Finished",
                              recipe_image_1='')
        self.recipe = Recipe.objects.first()

        # set recipe tags
        self.recipe.time_tags.set(CookTime.objects.all())
        self.recipe.allergies_tags.set(Allergies.objects.all())
        self.recipe.category_tags.set(Category.objects.all())
        self.recipe.equipment_tags.set(Equipment.objects.all())

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

    def test_get_first_last_cooking_time_tags(self):
        """
        Test first and last time tags.
        """
        self.assertEqual(str(CookTime.objects.first()), "10 Mins")
        self.assertEqual(str(CookTime.objects.last()), "1 Hour")

    def test_get_first_equipment_tags(self):
        """
        Test first and last equipment tags.
        """
        self.assertEqual(str(Equipment.objects.first()), "mixer")
        self.assertEqual(str(Equipment.objects.last()), "blender")

    def test_get_first_last_allergies_tags(self):
        """
        Test first and last allergies tags.
        """
        self.assertEqual(str(Allergies.objects.first()), "egg")
        self.assertEqual(str(Allergies.objects.last()), "soy")

    def test_get_first_category_tags(self):
        """
        Test first and last category tags.
        """
        self.assertEqual(str(Category.objects.first()), "Main Course")
        self.assertEqual(str(Category.objects.last()), "Main Course")

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

    def test_recipe_get_time_tags(self):
        """
        Test recipe time tags enable or not.
        """
        self.assertEqual(self.recipe.time_tags.count(), CookTime.objects.count())
        self.assertEqual(str(self.recipe.time_tags.first()), "10 Mins")
        self.assertEqual(str(self.recipe.time_tags.last()), "1 Hour")

    def test_recipe_get_equipment_tags(self):
        """
        Test recipe equipment tags enable or not.
        """
        self.assertEqual(self.recipe.equipment_tags.count(), Equipment.objects.count())
        self.assertEqual(str(self.recipe.equipment_tags.first()), "mixer")
        self.assertEqual(str(self.recipe.equipment_tags.last()), "blender")

    def test_recipe_get_allergies_tags(self):
        """
        Test recipe allergies tags enable or not.
        """
        self.assertEqual(self.recipe.allergies_tags.count(), Allergies.objects.count())
        self.assertEqual(str(self.recipe.allergies_tags.first()), "egg")
        self.assertEqual(str(self.recipe.allergies_tags.last()), "soy")

    def test_recipe_get_category_tags(self):
        """
        Test recipe time tags enable or not.
        """
        self.assertEqual(self.recipe.category_tags.count(), Category.objects.count())
        self.assertEqual(str(self.recipe.category_tags.first()), "Main Course")
        self.assertEqual(str(self.recipe.category_tags.last()), "Main Course")
