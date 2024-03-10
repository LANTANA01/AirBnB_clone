#!/usr/bin/python3
"""__init__ is use to initialize the package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
