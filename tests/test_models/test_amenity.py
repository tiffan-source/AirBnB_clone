#!/usr/bin/python3
"""
test_review module : Test behavior of Review Class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    TestAmenity - Test behavior of Amenity Class
    """

    def test_Base_class_documentation(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_module_base_documentation(self):
        import models.amenity
        self.assertIsNotNone(models.amenity.__doc__)
