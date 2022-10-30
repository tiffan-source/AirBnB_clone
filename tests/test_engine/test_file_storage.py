#!/usr/bin/python3
"""
test_file_storage module define TestFileStorage class
to test behavior of FileStorage class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

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

        self.assertTrue(f"{test_base.__class__.__name__}.{test_base.id}" in fs.all())
        self.assertEqual(test_base, fs.all()[f"{test_base.__class__.__name__}.{test_base.id}"])

        test_user = User()
        fs.new(test_user)

        self.assertTrue(f"{test_user.__class__.__name__}.{test_user.id}" in fs.all())
        self.assertEqual(test_user, fs.all()[f"{test_user.__class__.__name__}.{test_user.id}"])

    def test_save(self):
        fs = FileStorage()
        test_base = BaseModel()
        test_user = User()
        fs.new(test_base)
        fs.new(test_user)
        fs.save()
        fs.reload()

    # def test_reload(self):
    #     fs = FileStorage()
    #     fs.reload()
    #     obj = fs.all()
    #     self.assertNotEqual(0, len(obj))
