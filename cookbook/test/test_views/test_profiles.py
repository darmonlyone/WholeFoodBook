from django.test import TestCase
from django.urls import reverse

from cookbook.models import *
from cookbook.test.mock import mock_data


class TestProfile(TestCase):

    def test_profiles_status_code(self):
        """
        Test for check that page is work.

        """
        response = self.client.get(reverse('cookbook:profile'))
        self.assertEqual(response.status_code, 200)

    def test_profiles_contain(self):
        """
        Test check contain User profile.

        """
        response = self.client.get(reverse('cookbook:profile'))
        self.assertContains(response, "You haven't login yet")
