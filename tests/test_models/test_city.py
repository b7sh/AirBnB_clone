#!/usr/bin/python3
from time import sleep
from models.city import City
import unittest
import datetime
import io
import sys


class City_id(unittest.TestCase):
    """test the id of City"""
    def setUp(self):
        self.city1 = City()
        self.city2 = City()

    def test_is_basemodule(self):
        self.assertIsInstance(self.city1, City)

    def test_unique_id(self):
        self.assertNotEqual(self.city1.id, self.city2.id)

    def test_str_id(self):
        self.assertIsInstance(self.city1.id, str)
        self.assertIsInstance(self.city2.id, str)

    def test_city_attr(self):
        self.assertIsInstance(self.city1.state_id, str)
        self.assertIsInstance(self.city1.name, str)

class City_to_dict(unittest.TestCase):
    """test the dict of City"""
    def setUp(self):
        self.city1 = City()
        self.city2 = City()

    def test_to_dict(self):
        self.assertIsInstance(self.city1.to_dict(), dict)

    def test_key_in_dict(self):
        self.assertIn("id", self.city1.to_dict())
        self.assertIn("created_at", self.city1.to_dict())
        self.assertIn("updated_at", self.city1.to_dict())
        self.assertIn("__class__", self.city1.to_dict())

    def test_add_attr(self):
        self.city1.name = "omar"
        self.city1.my_number = 20
        self.assertIn("name", self.city1.to_dict())
        self.assertIn("my_number", self.city1.to_dict())


class City_datetime(unittest.TestCase):
    """test the datetime of City"""
    def setUp(self):
        self.city1 = City()
        self.city2 = City()

    def test_if_obj(self):
        self.assertIsInstance(self.city1.created_at, datetime.datetime)
        self.assertIsInstance(self.city1.updated_at, datetime.datetime)

    def test_if_str(self):
        dictionary = self.city1.to_dict()
        self.assertIsInstance(dictionary["updated_at"], str)
        self.assertIsInstance(dictionary["created_at"], str)


class City_save(unittest.TestCase):
    """test the save of City"""
    def setUp(self):
        self.city1 = City()
        self.city2 = City()

    def test_save(self):
        first_update = self.city1.updated_at
        sleep(0.01)
        self.city1.save()
        self.assertNotEqual(first_update, self.city1.updated_at)


class City_str(unittest.TestCase):
    """test the str of City"""
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
        self.city1 = City()
        self.city2 = City

    def test_print(self):
        capture = City_str.capture_stdout(self.city1)
        except_output = f"[{self.city1.__class__.__name__}] ({self.city1.id}) {self.city1.__dict__}\n"
        self.assertEqual(except_output,
                        capture.getvalue())

    def test_modify_class(self):
        modify = {"id": "55", "created_at": datetime.datetime.now().isoformat(),
                  "updated_at": datetime.datetime.now().isoformat()}
        new_base = self.city2(**modify)
        capture = City_str.capture_stdout(new_base)
        except_output = f"[{new_base.__class__.__name__}] ({new_base.id}) {new_base.__dict__}\n"
        self.assertEqual(except_output,
                        capture.getvalue())
