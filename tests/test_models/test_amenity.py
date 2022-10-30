#!/usr/bin/python3
"""
test_amenity module define TestAmenity class
to test behavior of Amenity class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    class TestAmenity
    test behavior of Amenity class
    """

    def test_amenity_class_documentation(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_module_amenity_documentation(self):
        import models.amenity
        self.assertIsNotNone(models.amenity.__doc__)

    def test_amenity_deriv_base(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_field(self):
        self.assertIsInstance(Amenity.name, str)

    def test_amenity_field_value(self):
        self.assertEqual("", Amenity.name)
