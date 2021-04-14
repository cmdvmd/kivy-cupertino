"""
A program to initialize all fonts used in Kivy Cupertino
"""

from kivy.core.text import LabelBase
from kivycupertino import fonts_path

fonts = [
    {
        "name": "San Francisco",
        "fn_regular": fonts_path + "sf.otf",
        "fn_italic": fonts_path + "sf-italic.otf",
        "fn_bold": fonts_path + "sf-bold.otf",
        "fn_bolditalic": fonts_path + "sf-bold-italic.otf",
    },
    {
        "name": "New York",
        "fn_regular": fonts_path + "ny.ttf",
        "fn_italic": fonts_path + "ny-italic.ttf",
        "fn_bold": fonts_path + "ny-bold.otf",
        "fn_bolditalic": fonts_path + "ny-bold-italic.otf",
    },
    {"name": "SF Symbols", "fn_regular": fonts_path + "sfsymbols.ttf"},
]

for font in fonts:
    LabelBase.register(**font)
