#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """ defien the user information"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
