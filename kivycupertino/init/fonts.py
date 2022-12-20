"""
A program to initialize all fonts used in Kivy Cupertino
"""

from kivycupertino import sf_path, ny_path, fonts_path
from kivy.core.text import LabelBase

fonts = [
    {
        'name': 'San Francisco',
        'fn_regular': sf_path + 'sf.otf',
        'fn_italic': sf_path + 'sf-italic.otf',
        'fn_bold': sf_path + 'sf-bold.otf',
        'fn_bolditalic': sf_path + 'sf-bold-italic.otf',
    },
    {
        'name': 'New York',
        'fn_regular': ny_path + 'ny.ttf',
        'fn_italic': ny_path + 'ny-italic.ttf',
        'fn_bold': ny_path + 'ny-bold.otf',
        'fn_bolditalic': ny_path + 'ny-bold-italic.otf',
    },
    {
        'name': 'SF Symbols',
        'fn_regular': fonts_path + 'sfsymbols.ttf'
    }
]

for font in fonts:
    LabelBase.register(**font)
