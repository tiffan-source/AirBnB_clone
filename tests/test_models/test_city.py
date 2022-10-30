#!/usr/bin/python3
"""
test_review module : Test behavior of Review Class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    TestCity - Test behavior of City Class
    """

    def test_Base_class_documentation(self):
        self.assertIsNotNone(City.__doc__)

    def test_module_base_documentation(self):
        import models.city
        self.assertIsNotNone(models.city.__doc__)
