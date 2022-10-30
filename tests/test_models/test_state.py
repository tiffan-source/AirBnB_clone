#!/usr/bin/python3
"""
test_state module : Test behavior of State Class
"""
import unittest
from models.state import State


class Deriv(State):
    """
    Class Deriv used to perform write test
    """
    pass


class TestState(unittest.TestCase):
    """
	TestState - Test behavior of State Class
    """

    def test_Base_class_documentation(self):
        self.assertIsNotNone(State.__doc__)

    def test_module_base_documentation(self):
        import models.state
        self.assertIsNotNone(models.state.__doc__)
