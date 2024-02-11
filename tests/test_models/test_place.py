#!/usr/bin/python3
from time import sleep
from models.place import Place
import unittest
import datetime
import io
import sys


class Place_id(unittest.TestCase):
    """test the id of Place"""
    def setUp(self):
        self.place1 = Place()
        self.place2 = Place()

    def test_is_basemodule(self):
        self.assertIsInstance(self.place1, Place)

    def test_unique_id(self):
        self.assertNotEqual(self.place1.id, self.place2.id)

    def test_str_id(self):
        self.assertIsInstance(self.place1.id, str)
        self.assertIsInstance(self.place2.id, str)

    def test_city_attr(self):
        self.assertIsInstance(self.place1.name, str)
        self.assertIsInstance(self.place1.amenity_ids, list)
        self.assertIsInstance(self.place1.city_id, str)
        self.assertIsInstance(self.place1.latitude, float)
        self.assertIsInstance(self.place1.max_guest, int)
        self.assertIsInstance(self.place1.number_bathrooms, int)
        self.assertIsInstance(self.place1.number_rooms, int)
        self.assertIsInstance(self.place1.price_by_night, int)
        self.assertIsInstance(self.place1.user_id, str)
        self.assertIsInstance(self.place1.description, str)
        self.assertIsInstance(self.place1.longitude, float)


class Place_to_dict(unittest.TestCase):
    """test the dict of Place"""
    def setUp(self):
        self.place1 = Place()
        self.place2 = Place()

    def test_to_dict(self):
        self.assertIsInstance(self.place1.to_dict(), dict)

    def test_key_in_dict(self):
        self.assertIn("id", self.place1.to_dict())
        self.assertIn("created_at", self.place1.to_dict())
        self.assertIn("updated_at", self.place1.to_dict())
        self.assertIn("__class__", self.place1.to_dict())

    def test_add_attr(self):
        self.place1.name = "omar"
        self.place1.my_number = 20
        self.assertIn("name", self.place1.to_dict())
        self.assertIn("my_number", self.place1.to_dict())


class Place_datetime(unittest.TestCase):
    """test the datetime of Place"""
    def setUp(self):
        self.place1 = Place()
        self.place2 = Place()

    def test_if_obj(self):
        self.assertIsInstance(self.place1.created_at, datetime.datetime)
        self.assertIsInstance(self.place1.updated_at, datetime.datetime)

    def test_if_str(self):
        dictionary = self.place1.to_dict()
        self.assertIsInstance(dictionary["updated_at"], str)
        self.assertIsInstance(dictionary["created_at"], str)


class Place_save(unittest.TestCase):
    """test the save of Place"""
    def setUp(self):
        self.place1 = Place()
        self.place2 = Place()

    def test_save(self):
        first_update = self.place1.updated_at
        sleep(0.01)
        self.place1.save()
        self.assertNotEqual(first_update, self.place1.updated_at)


class Place_str(unittest.TestCase):
    """test the str of Place"""
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
        self.place1 = Place()
        self.place2 = Place

    def test_print(self):
        capture = Place_str.capture_stdout(self.place1)
        except_output = f"[{self.place1.__class__.__name__}]\
            ({self.place1.id}) {self.place1.__dict__}\n"
        self.assertEqual(except_output,
                         capture.getvalue())

    def test_modify_class(self):
        modify = {"id": "55",
                  "created_at": datetime.datetime.now().isoformat(),
                  "updated_at": datetime.datetime.now().isoformat()}
        new_base = self.place2(**modify)
        capture = Place_str.capture_stdout(new_base)
        except_output = f"[{new_base.__class__.__name__}] ({new_base.id})\
            {new_base.__dict__}\n"
        self.assertEqual(except_output,
                         capture.getvalue())
