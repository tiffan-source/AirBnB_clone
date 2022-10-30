#!/usr/bin/python3
"""
test_city module define TestCity class
to test behavior of City class
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    class TestCity
    test behavior of City class
    """

    def test_City_class_documentation(self):
        self.assertIsNotNone(City.__doc__)

    def test_module_city_documentation(self):
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
