#!/usr/bin/python3
"""test for file storage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class testattribute(unittest.TestCase):
    """test class attribute"""

    def setUp(self):
        self.storage = FileStorage()
        self.base = BaseModel()

    def test_type(self):
        """test type of storage"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_oject(self):
        """test object attribute"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertIsNotNone(objects)


class testmethods(unittest.TestCase):
    """test method of file storage"""

    def setUp(self):
        self.storage = FileStorage()
        self.base = BaseModel()

    def test_new_no_arg(self):
        """dont pass argument to new method"""
        with self.assertRaisesRegex(TypeError,
                                    " missing 1 required positional argument"):
            self.storage.new()

    def test_new_with_arg(self):
        """pass obj to new method"""
        self.storage.new(self.base)
        objects = self.storage.all()
        expected = f"{self.base.__class__.__name__}.{self.base.id}"
        self.assertIn(expected, objects)

    def test_new_with_str(self):
        with self.assertRaisesRegex(AttributeError,
                                    "object has no attribute 'id'"):
            self.storage.new("obj")
