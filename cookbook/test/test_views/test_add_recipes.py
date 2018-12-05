from django.test import TestCase
from django.urls import reverse

from cookbook.models import *
from cookbook.test.mock import mock_data


class AddRecipeTest(TestCase):

    def test_add_recipe_status_code(self):
        """
        Test for check that add recipe page is work.
    
        """
        response = self.client.get(reverse('cookbook:addRecipe'))
        self.assertEqual(response.status_code, 200)

    def test_add_recipe_contain(self):
        """
        Test check that add recipe contain direction part.
        """
        response = self.client.get(reverse('cookbook:addRecipe'))
        self.assertContains(response, "You haven't login yet")
