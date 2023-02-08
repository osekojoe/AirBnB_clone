#!/usr/bin/python3

"""
The __init__.py file is used to mark a directory as a Python package.
It's executed when the package is imported, and it  contains initialization code for the package.
"""

from models.engine.file_storage import FileStorage 
""" importing filestorage.py from models folder"""


storage = FileStorage()
""" creating the variable storage, an instance of FileStorage """
storage.reload()
""" calling reload() method on storage variable """
