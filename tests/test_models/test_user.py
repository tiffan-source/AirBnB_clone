#!/usr/bin/python3
""" TestUser - Test behavior of User Class"""
from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestUser(TestBaseModel):
    """
    TestUser - Test behavior of User Class
    """

    def __init__(self, *args, **kwargs):
        """ Initialization of the TestUser class"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_User_class_documentation(self):
        """
        test User class documentation
        """
        self.assertIsNotNone(User.__doc__)

    def test_module_user_documentation(self):
        """ Check module user documentation """
        import models.user
        self.assertIsNotNone(models.user.__doc__)

    def test_first_name(self):
        """Check first name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Check last name"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_password(self):
        """Check password"""
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_email(self):
        """Check email"""
        new = self.value()
        self.assertEqual(type(new.email), str)
