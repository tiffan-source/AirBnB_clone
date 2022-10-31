#!/usr/bin/python3
"""
test_review module : Test behavior of Review Class
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    TestCity - Test behavior of City Class
    """

    def test_Base_class_documentation(self):
        self.assertIsNotNone(City.__doc__)

    def test_module_base_documentation(self):
        import models.city
        self.assertIsNotNone(models.city.__doc__)

    def test_city_deriv_base(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_field(self):
        self.assertIsInstance(City.state_id, str)
        self.assertIsInstance(City.name, str)

    def test_city_field_value(self):
        self.assertEqual("", City.name)
        self.assertEqual("", City.state_id)
