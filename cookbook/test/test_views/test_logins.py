from django.test import TestCase
from django.urls import reverse

from cookbook.models import *
from cookbook.test.mock import mock_data


class TestLogin(TestCase):

    def setUp(self):
        """
        Set up database for testing.
        """
        mock_data.set_data()

    def test_login_response(self):
        """
        Test check that index page is work.

        """
        response = self.client.get(reverse('cookbook:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_responser(self):
        """
        Test check contain Sign in.
        
        """
        response = self.client.get(reverse('cookbook:login'))
        self.assertContains(response, "Sign in")
