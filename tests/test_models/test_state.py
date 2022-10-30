#!/usr/bin/python3
"""
test_state module define TestState class
to test behavior of State class
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    class TestState
    test behavior of State class
    """

    def test_State_class_documentation(self):
        self.assertIsNotNone(State.__doc__)

    def test_module_state_documentation(self):
        import models.state
        self.assertIsNotNone(models.state.__doc__)

    def test_state_deriv_base(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_field(self):
        self.assertIsInstance(State.name, str)

    def test_state_field_value(self):
        self.assertEqual("", State.name)
