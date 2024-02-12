#!/usr/bin/python3
"""test for file storage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
import models


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
        """check the id attribute"""
        with self.assertRaisesRegex(AttributeError,
                                    "object has no attribute 'id'"):
            self.storage.new("obj")

    def test_new(self):
        b = BaseModel()
        u = User()
        c = City()
        s = State()
        p = Place()
        r = Review()
        a = Amenity()

        models.storage.new(b)
        models.storage.new(u)
        models.storage.new(c)
        models.storage.new(s)
        models.storage.new(p)
        models.storage.new(r)
        models.storage.new(a)

        self.assertIn(f"BaseModel.{b.id}", models.storage.all().keys())
        self.assertIn(b, models.storage.all().values())
        self.assertIn(f"User.{u.id}", models.storage.all().keys())
        self.assertIn(u, models.storage.all().values())
        self.assertIn(f"City.{c.id}", models.storage.all().keys())
        self.assertIn(c, models.storage.all().values())
        self.assertIn(f"State.{s.id}", models.storage.all().keys())
        self.assertIn(s, models.storage.all().values())
        self.assertIn(f"Place.{p.id}", models.storage.all().keys())
        self.assertIn(p, models.storage.all().values())
        self.assertIn(f"Review.{r.id}", models.storage.all().keys())
        self.assertIn(r, models.storage.all().values())
        self.assertIn(f"Amenity.{a.id}", models.storage.all().keys())
        self.assertIn(a, models.storage.all().values())
