#!/usr/bin/python3
"""
test_user module define TestUser class
to test behavior of User class
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    class TestUser
    test behavior of User class
    """

    def test_User_class_documentation(self):
        self.assertIsNotNone(User.__doc__)

    def test_module_user_documentation(self):
        import models.user
        self.assertIsNotNone(models.user.__doc__)

    def test_user_deriv_base(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_field(self):
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

    def test_user_field_value(self):
        self.assertEqual("", User.email)
        self.assertEqual("", User.password)
        self.assertEqual("", User.first_name)
        self.assertEqual("", User.last_name)
