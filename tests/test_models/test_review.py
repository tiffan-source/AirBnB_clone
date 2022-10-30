#!/usr/bin/python3
"""
test_review module define TestReview class
to test behavior of Review class
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    class TestReview
    test behavior of Review class
    """

    def test_review_class_documentation(self):
        self.assertIsNotNone(Review.__doc__)

    def test_module_review_documentation(self):
        import models.review
        self.assertIsNotNone(models.review.__doc__)

    def test_review_deriv_base(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_field(self):
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)

    def test_review_field_value(self):
        self.assertEqual("", Review.place_id)
        self.assertEqual("", Review.user_id)
        self.assertEqual("", Review.text)
