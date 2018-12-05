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
        self.assertEqual("egg", Allergies.objects.filter(allergies_ingredient="egg"))

    def test_allergy_shrimp(self):
        """
        Test filter tag shrimp
        """
        self.assertEqual("shrimp", Allergies.objects.filter(allergies_ingredient="shrimp"))

    def test_allergy_soy(self):
        """
        Test filter tag soy
        """
        self.assertEqual("soy", Allergies.objects.filter(allergies_ingredient="soy"))

    def test_allergy_milk(self):
        """
        Test filter tag milk
        """
        self.assertEqual("milk", Allergies.objects.filter(allergies_ingredient="milk"))

    def test_allergy_shellfish(self):
        """
        Test filter tag shellfish
        """
        self.assertEqual("shellfish", Allergies.objects.filter(allergies_ingredient="shellfish"))

    def test_allergy_nuts(self):
        """
        Test filter tag nuts
        """
        self.assertEqual("nuts", Allergies.objects.filter(allergies_ingredient="nuts"))
