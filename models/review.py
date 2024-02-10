#!/usr/bin/python3
"""define the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ define the review information"""
    place_id = ""
    user_id = ""
    text = ""
