#!/usr/bin/python3
from time import sleep
from models.base_model import BaseModel
import unittest
import datetime
import io
import sys


class BaseModel_id(unittest.TestCase):
    """test the id of basemodel"""
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
    """test the dict of basemodel"""
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
    """test the datetime of basemodel"""
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
    """test the save of basemodel"""
    def setUp(self):
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def test_save(self):
        first_update = self.base1.updated_at
        sleep(0.01)
        self.base1.save()
        self.assertNotEqual(first_update, self.base1.updated_at)


class BaseModel_str(unittest.TestCase):
    """test the str of basemodel"""
    @staticmethod
    def capture_stdout(clas):
        """Captures and returns text printed to stdout.

        Args:
            cls (class): The class to print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        print(clas)
        sys.stdout = sys.__stdout__
        return capture

    def setUp(self):
        self.base1 = BaseModel()
        self.base2 = BaseModel

    def test_print(self):
        capture = BaseModel_str.capture_stdout(self.base1)
        first = f"[{self.base1.__class__.__name__}] "
        except_output = first + f"({self.base1.id}) {self.base1.__dict__}\n"
        self.assertEqual(except_output,
                         capture.getvalue())

    def test_modify_class(self):
        modify = {"id": "55",
                  "created_at": datetime.datetime.now().isoformat(),
                  "updated_at": datetime.datetime.now().isoformat()}
        new_base = self.base2(**modify)
        capture = BaseModel_str.capture_stdout(new_base)
        first = f"[{new_base.__class__.__name__}] "
        except_output = first + f"({new_base.id}) {new_base.__dict__}\n"
        self.assertEqual(except_output,
                         capture.getvalue())
