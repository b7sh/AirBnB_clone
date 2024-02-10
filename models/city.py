#!/usr/bin/python3
""" define city module"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """representation of city information"""

    state_id = ""
    name = ""
