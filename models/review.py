#!/usr/bin/python3
"""Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """public class Review"""
    place_id = ""
    user_id = ""
    text = ""
