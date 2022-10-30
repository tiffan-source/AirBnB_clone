#!/usr/bin/python3
"""
test_place module define TestPlace class
to test behavior of Place class
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    class TestPlace
    test behavior of Place class
    """

    def test_place_class_documentation(self):
        self.assertIsNotNone(Place.__doc__)

    def test_module_place_documentation(self):
        import models.place
        self.assertIsNotNone(models.place.__doc__)

    def test_place_deriv_base(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_field(self):
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.amenity_ids, str)

    def test_place_field_value(self):
        self.assertEqual("", Place.city_id)
        self.assertEqual("", Place.user_id)
        self.assertEqual("", Place.name)
        self.assertEqual("", Place.description)
        self.assertEqual(0, Place.number_rooms)
        self.assertEqual(0, Place.number_bathrooms)
        self.assertEqual(0, Place.max_guest)
        self.assertEqual(0, Place.price_by_night)
        self.assertEqual(0.0, Place.latitude)
        self.assertEqual(0.0, Place.longitude)
        self.assertEqual("", Place.amenity_ids)
