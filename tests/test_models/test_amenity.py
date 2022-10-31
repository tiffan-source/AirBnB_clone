#!/usr/bin/python3
"""
test_review module : Test behavior of Review Class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    TestAmenity - Test behavior of Amenity Class
    """

    def test_Amenity_class_documentation(self):
        """
        test_Amenity_class_documentation - test doc inside class
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_module_ametiy_documentation(self):
        """
        test_module_ametiy_documentation - test amenity module doc
        """
        import models.amenity
        self.assertIsNotNone(models.amenity.__doc__)

    def test_amenity_deriv_base(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_field(self):
        self.assertIsInstance(Amenity.name, str)

    def test_amenity_field_value(self):
        self.assertEqual("", Amenity.name)
