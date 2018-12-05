from django.test import TestCase
from django.urls import reverse

from cookbook.models import *
from cookbook.test.mock import mock_data


class TestRecipe(TestCase):
    def setUp(self):
        """
        Set up database for testing.
        """
        mock_data.set_data()

    def test_recipe_status_code(self):
        """
        Test for check that page is work.

        """
        response = self.client.get(reverse('cookbook:recipe', args=['Cedar Plank Salmon']))
        self.assertEqual(response.status_code, 200)

    def test_recipe(self):
        """
        Test check that recipe name when you put, show the same.

        """
        response = self.client.get(reverse('cookbook:recipe', args=['Coconut Protein Balls']))
        self.assertContains(response, "Coconut Protein Balls")

    def test_recipe_name(self):
        """
        Test check that recipe name when you put, show the same.

        """
        response = self.client.get(reverse('cookbook:recipe', args=['Glowing Green Juice']))
        self.assertContains(response, "Glowing Green Juice")

    def test_recipe_time(self):
        """
        Test check that recipe show a time.

        """
        response = self.client.get(reverse('cookbook:recipe', args=['Glowing Green Juice']))
        self.assertContains(response, "TIME:")

    def test_recipe_equipment(self):
        """
        Test check that recipe show a equipment.

        """
        response = self.client.get(reverse('cookbook:recipe', args=['Glowing Green Juice']))
        self.assertContains(response, "EQUIPMENT:")
