import os

root = os.path.dirname(__file__)
fonts = os.path.join(root, 'fonts/')
icons = os.path.join(root, 'icons/')
images = os.path.join(root, 'images/')

from .init import fonts, widgets
