#!/usr/bin/python3
""" define city module"""
from models.base_model import BaseModel


class City(BaseModel):
    """representation of city information"""

    state_id = ""
    name = ""
