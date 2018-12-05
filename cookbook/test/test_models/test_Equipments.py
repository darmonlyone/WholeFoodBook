from django.test import TestCase

from cookbook.models import Equipment
from cookbook.test.mock.mock_data import ReadData
from cookbook.models import *
from cookbook.test.mock import mock_data


class EquipmentTest(TestCase):

    def test_equipment_amount(self):
        """
        Test amount of Equipment tags
        """
        self.assertEqual(4, Equipment.objects.count())

    def test_equipment_blender(self):
        """
        Test equipment blender filter
        """
        self.assertEqual("blender", Equipment.objects.get(equipment_required="blender").equipment_required)

    def test_equipment_mixer(self):
        """
        Test equipment mixer filter
        """
        self.assertEqual("mixer", Equipment.objects.get(equipment_required="mixer").equipment_required)

    def test_equipment_microwave(self):
        """
        Test equipment microwave filter
        """
        self.assertEqual("microwave", Equipment.objects.get(equipment_required="microwave").equipment_required)

    def test_equipment_oven(self):
        """
        Test equipment oven filter
        """
        self.assertEqual("oven", Equipment.objects.get(equipment_required="oven").equipment_required)
