from django.test import TestCase
from django.urls import reverse

from cookbook.models import *
from cookbook.test.mock import mock_data


class TestSearch(TestCase):
    def setUp(self):
        """
        Set up database for testing.
        """
        mock_data.set_data()

    def test_search_status_code(self):
        """
        Test for check that page is work.

        """
        response = self.client.get(reverse('cookbook:search', args=['Chicken']))
        self.assertEqual(response.status_code, 200)

    def test_seacrh_response(self):
        """
        Test recipe name when searching.

        """
        response = self.client.get(reverse('cookbook:search', args=['Chicken']))
        self.assertContains(response, "Searching for \"Chicken\"")

    def test_seacrh_chefname(self):
        """
        Test check chef name when searching.

        """
        response = self.client.get(reverse('cookbook:search', args=['Olena']))
        self.assertContains(response, "Recipe chef matched")

    def test_seacrh_recipe(self):
        """
        Test recipe name when searching.

        """
        response = self.client.get(reverse('cookbook:search', args=['Pumpkin']))
        self.assertContains(response, "Recipe name matched")

    def test_asd(self):
        """
        Test check that it's search.

        """
        response = self.client.get(reverse('cookbook:search', args=['Olena']))
        self.assertContains(response, "Searching for \"Olena\"")
