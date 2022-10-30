#!/usr/bin/python3
"""
test_file_storage module define TestFileStorage class
to test behavior of FileStorage class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    class TestFileStorage
    test behavior of FileStorage class
    """

    def test_module_doc(self):
        import models.engine.file_storage
        self.assertIsNotNone(models.engine.file_storage.__doc__)

    def test_file_storage_doc(self):
        self.assertIsNotNone(FileStorage.__doc__)

    def test_all_function_doc(self):
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_all_return_dict(self):
        new = FileStorage()
        self.assertIsInstance(new.all(), dict)

    def test_new_set_obj_and_all_get_it(self):
        fs = FileStorage()
        test_base = BaseModel()
        fs.new(test_base)

        key = test_base.__class__.__name__

        self.assertTrue(f"{key}.{test_base.id}" in fs.all())
        self.assertEqual(test_base, fs.all()[f"{key}.{test_base.id}"])

    def test_save(self):
        fs = FileStorage()
        test_base = BaseModel()
        fs.new(test_base)
        fs.save()
        fs.reload()
