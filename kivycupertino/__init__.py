import os

__version__ = '0.0.1-alpha'
__author__ = 'cmdmvd'
__copyright__ = 'Copyright (c) 2021, cmdvmd'
__license__ = 'MIT'

root = os.path.dirname(__file__)
fonts_path = os.path.join(root, 'fonts/')
icons_path = os.path.join(root, 'icons/')
images_path = os.path.join(root, 'images/')

from .init import fonts, widgets
