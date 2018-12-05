from django.test import TestCase

from cookbook.models import *
from cookbook.test.mock import mock_data


class AllergiesTest(TestCase):
    @classmethod
    def setUpClass(cls):
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
        alleries = Allergies.objects.get(allergies_ingredient="egg")
        self.assertEqual("egg", str(alleries.allergies_ingredient))

    def test_allergy_shrimp(self):
        """
        Test filter tag shrimp
        """
        allere = Allergies.objects.get(allergies_ingredient="shrimp")
        self.assertEqual("shrimp", str(allere.allergies_ingredient))

    def test_allergy_soy(self):
        """
        Test filter tag soy
        """
        aller = Allergies.objects.get(allergies_ingredient="soy")
        self.assertEqual("soy", aller.allergies_ingredient)

    def test_allergy_milk(self):
        """
        Test filter tag milk
        """
        aller = Allergies.objects.get(allergies_ingredient="milk")
        self.assertEqual("milk", str(aller.allergies_ingredient))

    def test_allergy_shellfish(self):
        """
        Test filter tag shellfish
        """
        self.assertEqual("shellfish", str(Allergies.objects.get(allergies_ingredient="shellfish").allergies_ingredient))

    def test_allergy_nuts(self):
        """
        Test filter tag nuts
        """
        self.assertEqual("nuts", str(Allergies.objects.get(allergies_ingredient="nuts").allergies_ingredient))

    @classmethod
    def tearDownClass(cls):
        pass
