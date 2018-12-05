from django.test import TestCase

from cookbook.models import CookTime
from cookbook.test.mock.mock_data import ReadData

from cookbook.models import *
from cookbook.test.mock import mock_data


class CooktimeTest(TestCase):

    def test_cooktime_amount(self):
        """
        Test amount of Cooktime tags
        """
        self.assertEqual(6, CookTime.objects.count())

    def test_cooktime_30min(self):
        """
        Test filter 30-min tag
        """
        self.assertEqual("30 min", CookTime.objects.get(cooking_time="30 min").cooking_time)

    def test_cooktime_morethan2hr(self):
        """
        Test filter more than 2 hr tag
        """
        self.assertEqual("2 hr", CookTime.objects.get(cooking_time="2 hr").cooking_time)

    def test_cooktime_2hr(self):
        """
        Test filter 2 hr tag
        """
        self.assertEqual("2 hr", CookTime.objects.get(cooking_time="2 hr").cooking_time)

    def test_cooktime_1hr30min(self):
        """
        Test filter 1hr30min tag
        """
        self.assertEqual("1 hr 30 min", CookTime.objects.get(cooking_time="1 hr 30 min").cooking_time)

    def test_cooktime_1hr(self):
        """
        Test filter 1hr tag
        """
        self.assertEqual("1 hr", CookTime.objects.get(cooking_time="1 hr").cooking_time)

    def test_cooktime_15min(self):
        """
        Test filter 15 min tag
        """
        self.assertEqual("15 min", CookTime.objects.get(cooking_time="15 min").cooking_time)
