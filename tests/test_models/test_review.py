#!/usr/bin/python3
from time import sleep
from models.base_model import Review
import unittest
import datetime
import io
import sys


class Review_id(unittest.TestCase):
    """test the id of Review"""
    def setUp(self):
        self.review1 = Review()
        self.review2 = Review()

    def test_is_basemodule(self):
        self.assertIsInstance(self.review1, Review)

    def test_unique_id(self):
        self.assertNotEqual(self.review1.id, self.review2.id)

    def test_str_id(self):
        self.assertIsInstance(self.review1.id, str)
        self.assertIsInstance(self.review2.id, str)

    
    def test_review_atrr(self):
        self.assertIsInstance(self.review2.place_id, str)
        self.assertIsInstance(self.review2.user_id, str)
        self.assertIsInstance(self.review2.text, str)


class Review_to_dict(unittest.TestCase):
    """test the dict of Review"""
    def setUp(self):
        self.review1 = Review()
        self.review2 = Review()

    def test_to_dict(self):
        self.assertIsInstance(self.review1.to_dict(), dict)

    def test_key_in_dict(self):
        self.assertIn("id", self.review1.to_dict())
        self.assertIn("created_at", self.review1.to_dict())
        self.assertIn("updated_at", self.review1.to_dict())
        self.assertIn("__class__", self.review1.to_dict())

    def test_add_attr(self):
        self.review1.name = "omar"
        self.review1.my_number = 20
        self.assertIn("name", self.review1.to_dict())
        self.assertIn("my_number", self.review1.to_dict())


class Review_datetime(unittest.TestCase):
    """test the datetime of Review"""
    def setUp(self):
        self.review1 = Review()
        self.review2 = Review()

    def test_if_obj(self):
        self.assertIsInstance(self.review1.created_at, datetime.datetime)
        self.assertIsInstance(self.review1.updated_at, datetime.datetime)

    def test_if_str(self):
        dictionary = self.review1.to_dict()
        self.assertIsInstance(dictionary["updated_at"], str)
        self.assertIsInstance(dictionary["created_at"], str)


class Review_save(unittest.TestCase):
    """test the save of Review"""
    def setUp(self):
        self.review1 = Review()
        self.review2 = Review()

    def test_save(self):
        first_update = self.review1.updated_at
        sleep(0.01)
        self.review1.save()
        self.assertNotEqual(first_update, self.review1.updated_at)


class Review_str(unittest.TestCase):
    """test the str of Review"""
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
        self.review1 = Review()
        self.review2 = Review

    def test_print(self):
        capture = Review_str.capture_stdout(self.review1)
        except_output = f"[{self.review1.__class__.__name__}] ({self.review1.id}) {self.review1.__dict__}\n"
        self.assertEqual(except_output,
                        capture.getvalue())

    def test_modify_class(self):
        modify = {"id": "55", "created_at": datetime.datetime.now().isoformat(),
                  "updated_at": datetime.datetime.now().isoformat()}
        new_base = self.review2(**modify)
        capture = Review_str.capture_stdout(new_base)
        except_output = f"[{new_base.__class__.__name__}] ({new_base.id}) {new_base.__dict__}\n"
        self.assertEqual(except_output,
                        capture.getvalue())
