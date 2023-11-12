#!/usr/bin/python3
""" module for review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ class of review """
    place_id = ""
    user_id = ""
    text = ""
