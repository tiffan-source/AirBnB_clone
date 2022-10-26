#!/usr/bin/python3
"""
test_base_model module define TestBaseModel class
to test behavior of BaseModel class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4

"""
class Deriv use to perform write test
"""

class Deriv(BaseModel):
    pass

"""
class TestBaseModel
test behavior of BaseModel class
"""
class TestBaseModel(unittest.TestCase):

    def test_Base_class_documentation(self):
        self.assertIsNotNone(BaseModel.__doc__)

    def test_module_base_documentation(self):
        import models.base_model
        self.assertIsNotNone(models.base_model.__doc__)

    def test_init_pass_with_kwargs(self):
        dct = {}
        dct["id"] = "nouvel-id"
        dct["updated_at"] = datetime(2000, 1, 1)
        dct["created_at"] = datetime(2000, 1, 1)
        dct["another_key"] = "another_value"

        bsmodel = BaseModel(dct)
        self.assertEqual("nouvel-id", bsmodel.id)
        self.assertEqual("another_value", bsmodel.another_key)
        self.assertEqual(datetime(2000, 1, 1), bsmodel.updated_at)
        self.assertEqual(datetime(2000, 1, 1), bsmodel.created_at)

    def test_id_instance_exist(self):
        elt = BaseModel()
        self.assertTrue("id" in elt.__dict__)

    def test_id_instance_type(self):
        elt = BaseModel()
        self.assertTrue(isinstance(elt.id, str))

    def test_unique_id_for_two_instance(self):
        elt1 = BaseModel()
        elt2 = BaseModel()
        self.assertNotEqual(elt1.id, elt2.id)

    def test_created_at_exist(self):
        elt = BaseModel()
        self.assertTrue("created_at" in elt.__dict__)

    def test_created_at_type(self):
        elt = BaseModel()
        self.assertTrue(isinstance(elt.created_at, datetime))

    def test_created_at_value_when_instance_create(self):
        elt = BaseModel()
        istancedate = elt.created_at.strftime("%Y%b%d%H%M")
        currentdate = datetime.now().strftime("%Y%b%d%H%M")
        self.assertEqual(istancedate, currentdate)

    def test_updated_at_exist(self):
        elt = BaseModel()
        self.assertTrue("updated_at" in elt.__dict__)

    def test_updated_at_type(self):
        elt = BaseModel()
        self.assertTrue(isinstance(elt.updated_at, datetime))

    def test_updated_at_same_as_create_at_when_instance_declare(self):
        elt = BaseModel()
        self.assertEqual(elt.updated_at, elt.created_at)

    def test_str_documentation(self):
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def test_str_value_for_instance(self):
        elt = BaseModel()
        self.assertEqual(elf.str(), f"[BaseModel] ({elt.id}) {elt.__dict__}")

    def test_str_value_for_instance_derivate_of_base(self):
        elt = Deriv()
        self.assertEqual(elf.str(), f"[Deruv] ({elt.id}) {elt.__dict__}")

    def test_save_documentation(self):
        self.assertIsNotNone(BaseModel.save.__doc__)

    def test_update_at_after_save(self):
        elt = BaseModel()
        prev = elt.updated_at
        t = 99999999999 + 999999999 #Just to pass moment
        elt.save()
        cur = elt.updated_at
        self.assertNotEqual(prev, cur)

    def test_to_dict_documentation(self):
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_to_dict_return_type(self):
        elt = BaseModel()
        self.assertTrue(isinstance(elt.to_dict(), dict))
