#!/usr/bin/python3
"""define the place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ define class of place and information"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
