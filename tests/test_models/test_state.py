#!/usr/bin/python3
from time import sleep
from models.state import State
import unittest
import datetime
import io
import sys


class State_id(unittest.TestCase):
    """test the id of State"""
    def setUp(self):
        self.state1 = State()
        self.state2 = State()

    def test_is_basemodule(self):
        self.assertIsInstance(self.state1, State)

    def test_unique_id(self):
        self.assertNotEqual(self.state1.id, self.state2.id)

    def test_str_id(self):
        self.assertIsInstance(self.state1.id, str)
        self.assertIsInstance(self.state2.id, str)

    def test_state_attr(self):
        self.assertIsInstance(self.state1.name, str)


class State_to_dict(unittest.TestCase):
    """test the dict of State"""
    def setUp(self):
        self.state1 = State()
        self.state2 = State()

    def test_to_dict(self):
        self.assertIsInstance(self.state1.to_dict(), dict)

    def test_key_in_dict(self):
        self.assertIn("id", self.state1.to_dict())
        self.assertIn("created_at", self.state1.to_dict())
        self.assertIn("updated_at", self.state1.to_dict())
        self.assertIn("__class__", self.state1.to_dict())

    def test_add_attr(self):
        self.state1.name = "omar"
        self.state1.my_number = 20
        self.assertIn("name", self.state1.to_dict())
        self.assertIn("my_number", self.state1.to_dict())


class State_datetime(unittest.TestCase):
    """test the datetime of State"""
    def setUp(self):
        self.state1 = State()
        self.state2 = State()

    def test_if_obj(self):
        self.assertIsInstance(self.state1.created_at, datetime.datetime)
        self.assertIsInstance(self.state1.updated_at, datetime.datetime)

    def test_if_str(self):
        dictionary = self.state1.to_dict()
        self.assertIsInstance(dictionary["updated_at"], str)
        self.assertIsInstance(dictionary["created_at"], str)


class State_save(unittest.TestCase):
    """test the save of State"""
    def setUp(self):
        self.state1 = State()
        self.state2 = State()

    def test_save(self):
        first_update = self.state1.updated_at
        sleep(0.01)
        self.state1.save()
        self.assertNotEqual(first_update, self.state1.updated_at)


class State_str(unittest.TestCase):
    """test the str of State"""
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
        self.state1 = State()
        self.state2 = State

    def test_print(self):
        capture = State_str.capture_stdout(self.state1)
        except_output = f"[{self.state1.__class__.__name__}]\
            ({self.state1.id}) {self.state1.__dict__}\n"
        self.assertEqual(except_output,
                         capture.getvalue())

    def test_modify_class(self):
        modify = {"id": "55",
                  "created_at": datetime.datetime.now().isoformat(),
                  "updated_at": datetime.datetime.now().isoformat()}
        new_base = self.state2(**modify)
        capture = State_str.capture_stdout(new_base)
        except_output = f"[{new_base.__class__.__name__}]\
            ({new_base.id}) {new_base.__dict__}\n"
        self.assertEqual(except_output,
                         capture.getvalue())
