import os

__version__ = '0.0.1'
__author__ = 'cmdmvd'
__license__ = 'MIT'

root = os.path.dirname(__file__)
fonts_path = os.path.join(root, 'fonts/')
icons_path = os.path.join(root, 'icons/')
images_path = os.path.join(root, 'images/')

from .init import fonts, widgets
