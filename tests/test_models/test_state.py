#!/usr/bin/python3
""" TestState - Test behavior of User Class"""
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """
    TestState - Test behavior of State Class
    """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_Base_class_documentation(self):
        self.assertIsNotNone(State.__doc__)

    def test_module_base_documentation(self):
        import models.state
        self.assertIsNotNone(models.state.__doc__)

    def test_name(self):
        """ Check Name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
