"""
A program to initialize Kivy Cupertino
"""

import os

__author__ = 'cmdmvd'
__copyright__ = '2021, cmdvmd'
__version__ = '0.0.1-alpha'
__license__ = 'MIT'

root = os.path.dirname(__file__)
fonts_path = os.path.join(root, 'fonts/')
icons_path = os.path.join(root, 'icons/')
images_path = os.path.join(root, 'images/')

from .init import fonts, widgets
