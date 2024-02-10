#!/usr/bin/python3
from time import sleep
from models.base_model import User
import unittest
import datetime
import io
import sys


class User_id(unittest.TestCase):
    """test the id of User"""
    def setUp(self):
        self.base1 = User()
        self.base2 = User()

    def test_is_basemodule(self):
        self.assertIsInstance(self.base1, User)

    def test_unique_id(self):
        self.assertNotEqual(self.base1.id, self.base2.id)

    def test_str_id(self):
        self.assertIsInstance(self.base1.id, str)
        self.assertIsInstance(self.base2.id, str)


class User_to_dict(unittest.TestCase):
    """test the dict of User"""
    def setUp(self):
        self.base1 = User()
        self.base2 = User()

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


class User_datetime(unittest.TestCase):
    """test the datetime of User"""
    def setUp(self):
        self.base1 = User()
        self.base2 = User()

    def test_if_obj(self):
        self.assertIsInstance(self.base1.created_at, datetime.datetime)
        self.assertIsInstance(self.base1.updated_at, datetime.datetime)

    def test_if_str(self):
        dictionary = self.base1.to_dict()
        self.assertIsInstance(dictionary["updated_at"], str)
        self.assertIsInstance(dictionary["created_at"], str)


class User_save(unittest.TestCase):
    """test the save of User"""
    def setUp(self):
        self.base1 = User()
        self.base2 = User()

    def test_save(self):
        first_update = self.base1.updated_at
        sleep(0.01)
        self.base1.save()
        self.assertNotEqual(first_update, self.base1.updated_at)


class User_str(unittest.TestCase):
    """test the str of User"""
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
        self.base1 = User()
        self.base2 = User

    def test_print(self):
        capture = User_str.capture_stdout(self.base1)
        except_output = f"[{self.base1.__class__.__name__}] ({self.base1.id}) {self.base1.__dict__}\n"
        self.assertEqual(except_output,
                        capture.getvalue())

    def test_modify_class(self):
        modify = {"id": "55", "created_at": datetime.datetime.now().isoformat(),
                  "updated_at": datetime.datetime.now().isoformat()}
        new_base = self.base2(**modify)
        capture = User_str.capture_stdout(new_base)
        except_output = f"[{new_base.__class__.__name__}] ({new_base.id}) {new_base.__dict__}\n"
        self.assertEqual(except_output,
                        capture.getvalue())
