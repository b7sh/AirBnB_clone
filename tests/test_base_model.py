from time import sleep
import unittest
from models.base_model import BaseModel
import datetime
import os


class BaseModel_id(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def setUp(self):
        self.base1 = BaseModel()
        self.base2 = BaseModel()
    
    def test_is_basemodule(self):
        self.assertIsInstance(self.base1, BaseModel)

    def test_unique_id(self):
        self.assertNotEqual(self.base1.id, self.base2.id)
    
    def test_str_id(self):
        self.assertIsInstance(self.base1.id, str)
        self.assertIsInstance(self.base2.id, str)
    
class BaseModel_to_dict(unittest.TestCase):
    
    def setUp(self):
        self.base1 = BaseModel()
        self.base2 = BaseModel()
    

    def test_to_dict(self):
        self.assertIsInstance(self.base1.to_dict(), dict)
    
    def test_key_in_dict(self):
        self.assertIn("id", self.base1.to_dict())
        self.assertIn("created_at", self.base1.to_dict())
        self.assertIn("updated_at", self.base1.to_dict())
        self.assertIn("__class__", self.base1.to_dict())
    
    def test_add_attr(self):
        self.base1.name = "omar"
        self.base1.my_number = 20
        self.assertIn("name", self.base1.to_dict())
        self.assertIn("my_number", self.base1.to_dict())
    
class BaseModel_datetime(unittest.TestCase):
    
    def setUp(self):
        self.base1 = BaseModel()
        self.base2 = BaseModel()
        
    def test_if_obj(self):
        self.assertIsInstance(self.base1.created_at, datetime.datetime)
        self.assertIsInstance(self.base1.updated_at, datetime.datetime)

    def test_if_str(self):
        dictionary = self.base1.to_dict()
        self.assertIsInstance(dictionary["updated_at"], str)
        self.assertIsInstance(dictionary["created_at"], str)
        
class BaseModel_save(unittest.TestCase):
    
    def setUp(self):
        self.base1 = BaseModel()
        self.base2 = BaseModel()
        
    def test_save(self):
        first_update = self.base1.updated_at
        sleep(0.01)
        self.base1.save()
        self.assertNotEqual(first_update, self.base1.updated_at)
    
class BaseModel_str(unittest.TestCase):
    
    def setUp(self):
        print("to be continue")