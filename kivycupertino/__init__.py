"""
A program to initialize Kivy Cupertino
"""

import os

__author__ = 'cmdvmd'
__copyright__ = '2021, cmdvmd'
__version__ = '0.1.1-beta'
__license__ = 'MIT'

root_path = os.path.dirname(__file__) + '/'
fonts_path = os.path.join(root_path, 'fonts/')
icons_path = os.path.join(root_path, 'icons/')
images_path = os.path.join(root_path, 'images/')

from .init import fonts, widgets
