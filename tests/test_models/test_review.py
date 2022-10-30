#!/usr/bin/python3
"""
test_review module : Test behavior of Review Class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    TestReview - Test behavior of Review Class
    """

    def test_Base_class_documentation(self):
        self.assertIsNotNone(Review.__doc__)

    def test_module_base_documentation(self):
        import models.review
        self.assertIsNotNone(models.review.__doc__)
