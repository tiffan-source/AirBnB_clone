#!/usr/bin/python3
""" TestState - Test behavior of User Class"""
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """ TestReview - Test behavior of Review Class """

    def __init__(self, *args, **kwargs):
        """ Initialization of TestReview class """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_Base_class_documentation(self):
        """ Class Documentation """
        self.assertIsNotNone(Review.__doc__)

    def test_module_base_documentation(self):
        """ Base Documentation """
        import models.review
        self.assertIsNotNone(models.review.__doc__)

    def test_place_id(self):
        """ Test Place Id """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test User Id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Test Text """
        new = self.value()
        self.assertEqual(type(new.text), str)
