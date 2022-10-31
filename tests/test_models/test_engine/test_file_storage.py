#!/usr/bin/python3
"""
test_file_storage module define TestFileStorage class
to test behavior of FileStorage class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
from os.path import exists


class TestFileStorage(unittest.TestCase):
    """
    class TestFileStorage
    test behavior of FileStorage class
    """

    def setUp(self):
        with open(FileStorage._FileStorage__file_path, "w") as fle:
            fle.write("")

#    def tearDown(self):

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

    # def test_all_return_dict_value(self):
    #     pass

    def test_reload(self):
        t_b = BaseModel()
        t_u = User()

        fs = FileStorage()
        fs.new(t_b)
        fs.new(t_u)

        fs.save()

        fs.reload()

        true_data = FileStorage._FileStorage__objects

        id_u = f"User.{t_u.id}"
        id_b = f"BaseModel.{t_b.id}"
        self.assertIn(id_u, true_data)
        self.assertIn(id_b, true_data)

    def test_new_set_obj_and_all_get_it(self):
        fs = FileStorage()
        test_base = BaseModel()
        fs.new(test_base)

        key = test_base.__class__.__name__

        self.assertTrue(f"{key}.{test_base.id}" in fs.all())
        self.assertEqual(test_base, fs.all()[f"{key}.{test_base.id}"])

    def test_save_record_data_in_file(self):
        fs = FileStorage()
        t_b = BaseModel()
        fs.new(t_b)
        fs.save()

        with open(FileStorage._FileStorage__file_path, "r") as fle:
            line_to_test = fle.readline()
            tab_to_verif = line_to_test.split("\"")
            self.assertIn(f"BaseModel.{t_b.id}", tab_to_verif)
            date_up = f"{datetime.isoformat(t_b.updated_at)}"
            date_cr = f"{datetime.isoformat(t_b.created_at)}"
            self.assertIn(date_up, tab_to_verif)
            self.assertIn(date_cr, tab_to_verif)

    def test_file_exist_after_save(self):
        fs = FileStorage()
        t_b = BaseModel()
        fs.new(t_b)
        fs.save()

        self.assertTrue(exists(FileStorage._FileStorage__file_path))
    # def test_save(self):
    #     fs = FileStorage()
    #     test_base = BaseModel()
    #     fs.new(test_base)
    #     fs.save()
    #     fs.reload()
