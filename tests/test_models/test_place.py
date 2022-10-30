#!/usr/bin/python3
"""
test_review module : Test behavior of Review Class
"""
import unittest
from models.place import Place


class Deriv(Place):
    """
    Class Deriv used to perform write test
    """
    pass


class TestPlace(unittest.TestCase):
    """
	TestPlace - Test behavior of Place Class
    """

    def test_Base_class_documentation(self):
        self.assertIsNotNone(Place.__doc__)

    def test_module_base_documentation(self):
        import models.place
        self.assertIsNotNone(models.place.__doc__)
