import os
from kivy.core.text import LabelBase

root = os.path.dirname(__file__)
icons = os.path.join(root, 'icons/')
fonts = os.path.join(root, 'fonts/')

for font in os.listdir(fonts):
    LabelBase.register(font, f'{fonts}{font}/regular.ttf', f'{fonts}{font}/italic.ttf', f'{fonts}{font}/bold.otf', f'{fonts}{font}/bold_italic.otf')
