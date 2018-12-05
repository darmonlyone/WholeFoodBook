from django.test import TestCase

from cookbook.models import *
from cookbook.test.mock import mock_data


class AllergiesTest(TestCase):
    def setUp(self):
        """
        Set up database for testing.
        """
        mock_data.set_data()

    def test_allergies_amount(self):
        """
        Test amount of allergies
        """
        self.assertEqual(6, Allergies.objects.count())

    def test_allergy_egg(self):
        """
        Test filter tag egg
        """
        self.assertEqual("egg", Allergies.objects.get(allergies_ingredient="egg").allergies_ingredient)

    def test_allergy_shrimp(self):
        """
        Test filter tag shrimp
        """
        self.assertEqual("shrimp", Allergies.objects.get(allergies_ingredient="shrimp").allergies_ingredient)

    def test_allergy_soy(self):
        """
        Test filter tag soy
        """
        self.assertEqual("soy", Allergies.objects.get(allergies_ingredient="soy").allergies_ingredient)

    def test_allergy_milk(self):
        """
        Test filter tag milk
        """
        self.assertEqual("milk", Allergies.objects.get(allergies_ingredient="milk").allergies_ingredient)

    def test_allergy_shellfish(self):
        """
        Test filter tag shellfish
        """
        self.assertEqual("shellfish", Allergies.objects.get(allergies_ingredient="shellfish").allergies_ingredient)

    def test_allergy_nuts(self):
        """
        Test filter tag nuts
        """
        self.assertEqual("nuts", Allergies.objects.get(allergies_ingredient="nuts").allergies_ingredient)
