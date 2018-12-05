from django.test import TestCase
from django.urls import reverse

from cookbook.models import *
from cookbook.test.mock import mock_data


class TestWelcome(TestCase):
    def setUp(self):
        """
        Set up database for testing.
        """
        mock_data.set_data()

    def test_welcome_status_code(self):
        """
        Test for check that welcome page is work.

        """
        response = self.client.get(reverse('cookbook:welcome'))
        self.assertEqual(response.status_code, 200)

    def test_welcome_check_word(self):
        """
        Test check word on welcome page.

        """
        response = self.client.get(reverse('cookbook:welcome'))
        self.assertContains(response, "Welcome")
