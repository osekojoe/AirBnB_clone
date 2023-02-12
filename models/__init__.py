#!/usr/bin/python3

"""
The __init__.py file is used to mark a directory as a Python package.
It's executed when the package is imported, and it  contains initialization
code for the package.
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
