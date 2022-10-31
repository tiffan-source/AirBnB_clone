#!/usr/bin/python3
"""
test_base_model module define TestBaseModel class
to test behavior of BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4


class TestBaseModel(unittest.TestCase):
    """
    class TestBaseModel
    test behavior of BaseModel class
    """

    def test_Base_class_documentation(self):
        """
        test_Base_class_documentation - test Base doc
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_module_base_documentation(self):
        """
        test_module_base_documentation - test base module doc
        """
        import models.base_model
        self.assertIsNotNone(models.base_model.__doc__)

    def test_init_pass_with_kwargs(self):
        """
        test_init_pass_with_kwargs - test init pass with kwargs
        """
        dct = {}
        dct["id"] = "nouvel-id"
        dct["updated_at"] = datetime(2000, 1, 1).isoformat()
        dct["created_at"] = datetime(2000, 1, 1).isoformat()
        dct["another_key"] = "another_value"

        bsmodel = BaseModel(**dct)
        self.assertEqual("nouvel-id", bsmodel.id)
        self.assertEqual("another_value", bsmodel.another_key)
        self.assertEqual(datetime(2000, 1, 1), bsmodel.updated_at)
        self.assertEqual(datetime(2000, 1, 1), bsmodel.created_at)

    def test_id_instance_exist(self):
        """
        test_id_instance_exist - test id instance exit
        """
        elt = BaseModel()
        self.assertTrue("id" in elt.__dict__)

    def test_id_instance_type(self):
        """
        test_id_instance_type - test id instance type
        """
        elt = BaseModel()
        self.assertTrue(isinstance(elt.id, str))

    def test_unique_id_for_two_instance(self):
        """
        test_unique_id_for_two_instance - test uniqu id is set
        """
        elt1 = BaseModel()
        elt2 = BaseModel()
        self.assertNotEqual(elt1.id, elt2.id)

    def test_created_at_exist(self):
        """
        test_created_at_exist - test created_at exit
        """
        elt = BaseModel()
        self.assertTrue("created_at" in elt.__dict__)

    def test_created_at_type(self):
        """
        test_created_at_type - test created_at exist
        """
        elt = BaseModel()
        self.assertTrue(isinstance(elt.created_at, datetime))

    def test_created_at_value_when_instance_create(self):
        """
        test_created_at_value_when_instance_create - test created at value
        when instance create
        """
        elt = BaseModel()
        istancedate = elt.created_at.strftime("%Y%b%d%H%M")
        currentdate = datetime.now().strftime("%Y%b%d%H%M")
        self.assertEqual(istancedate, currentdate)

    def test_updated_at_exist(self):
        """
        test_updated_at_exist - test updated_at exist
        """
        elt = BaseModel()
        self.assertTrue("updated_at" in elt.__dict__)

    def test_updated_at_type(self):
        """
        test_updated_at_type - test updated_at type
        """
        elt = BaseModel()
        self.assertTrue(isinstance(elt.updated_at, datetime))

    def test_updated_at_same_as_create_at_when_instance_declare(self):
        """
        test_updated_at_same_as_create_at_when_instance_declare - test
        updated_at same as create_at when instance declare
        """
        elt = BaseModel()
        self.assertEqual(elt.updated_at, elt.created_at)

    def test_str_documentation(self):
        """
        test_str_documentation - test str documentation
        """
        self.assertIsNotNone(BaseModel.__str__.__doc__)

    def test_str_value_for_instance(self):
        """
        test_str_value_for_instance - test str value for instance
        """
        elt = BaseModel()
        self.assertEqual(str(elt), f"[BaseModel] ({elt.id}) {elt.__dict__}")

    def test_save_documentation(self):
        """
        test_save_documentation - test save documentation
        """
        self.assertIsNotNone(BaseModel.save.__doc__)

    def test_update_at_after_save(self):
        """
        test_update_at_after_save - test update_at after save
        """
        elt = BaseModel()
        prev = elt.updated_at
        t = 99999999999 + 999999999  # Just to pass moment
        elt.save()
        cur = elt.updated_at
        self.assertNotEqual(prev, cur)

    def test_to_dict_documentation(self):
        """
        test_to_dict_documentation - test to_dict documentation
        """
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_to_dict_return_type(self):
        """
        test_to_dict_return_type - test to_dict return type
        """
        elt = BaseModel()
        self.assertTrue(isinstance(elt.to_dict(), dict))

    def test_class_add_after_to_dict(self):
        """
        test that __class__ is add after to_dict method
        """
        elt = BaseModel()
        dict_result = elt.to_dict()
        self.assertTrue("__class__" in dict_result)
