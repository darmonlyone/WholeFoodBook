from django.test import TestCase

from cookbook.models import Category
from cookbook.test.mock.mock_data import ReadData
from cookbook.models import *
from cookbook.test.mock import mock_data


class CategoriesTest(TestCase):

    def test_categories_amount(self):
        """
        Test amount of category tags
        """
        self.assertEqual(6, Category.objects.count())

    def test_categories_drink(self):
        """
        Test categories drink filter
        """
        self.assertEqual("drink", Category.objects.get(food_category="drink").food_category)

    def test_categories_dessert(self):
        """
        Test categories dessert filter
        """
        self.assertEqual("dessert", Category.objects.get(food_category="dessert").food_category)

    def test_categories_soup(self):
        """
        Test categories soup and stew filter
        """
        self.assertEqual("soup and stew", Category.objects.get(food_category="soup and stew").food_category)

    def test_categories_main(self):
        """
        Test categories main dish filter
        """
        self.assertEqual("main dish", Category.objects.get(food_category="main dish").food_category)

    def test_categories_salad(self):
        """
        Test categories salad filter
        """
        self.assertEqual("salad", Category.objects.get(food_category="salad").food_category)

    def test_categories_appetizer(self):
        """
        Test categories appetizer filter
        """
        self.assertEqual("appetizer", Category.objects.get(food_category="appetizer").food_category)
