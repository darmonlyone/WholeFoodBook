from django.test import TestCase
from django.urls import reverse

from cookbook.models import *
from cookbook.test.mock import mock_data


class TestIndex(TestCase):

    def test_index_status_code(self):
        """
        Test for check that welcome page is work.

        """
        response = self.client.get(reverse('cookbook:index'))
        self.assertEqual(response.status_code, 200)

    def test_filter(self):
        """
        Test check that it's have filter.
    
        """
        response = self.client.get(reverse('cookbook:index'))
        self.assertContains(response, "TIME PREP")

    def test_catergory(self):
        """
        Test check that it's have category.
    
        """
        response = self.client.get(reverse('cookbook:index'))
        self.assertContains(response, "Salad")

    def test_allergise(self):
        """
        Test check that page have allergise.
    
        """
        response = self.client.get(reverse('cookbook:index'))
        self.assertContains(response, "ALLERGIES")

    def test_suggesttion(self):
        """
        Test check that page show the suggestion.
    
        """
        response = self.client.get(reverse('cookbook:index'))
        self.assertContains(response, "SUGGESTION")
