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
        base_model = BaseModel()
        user = User()
        city = City()
        state = State()
        place = Place()
        review = Review()
        amenity = Amenity()

        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(city)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(review)
        models.storage.new(amenity)

        self.assertIn("BaseModel." + base_model.id,
                       models.storage.all().keys())
        self.assertIn(base_model, models.storage.all().values())
        self.assertIn("User." + user.id,
                       models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        self.assertIn("City." + city.id,
                       models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn("State." + state.id,
                       models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("Place." + place.id,
                       models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("Review." + review.id,
                       models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())
        self.assertIn("Amenity." + amenity.id,
                       models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())
