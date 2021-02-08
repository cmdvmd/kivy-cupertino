from kivycupertino import fonts
from kivy.core.text import LabelBase

fonts = [
    {
        'name': 'San Francisco',
        'fn_regular': fonts+'sf.ttf',
        'fn_italic': fonts+'sf-italic.ttf',
        'fn_bold': fonts+'sf-bold.otf',
        'fn_bolditalic': fonts+'sf-bold-italic.otf',
    },
    {
        'name': 'New York',
        'fn_regular': fonts+'ny.ttf',
        'fn_italic': fonts+'ny-italic.ttf',
        'fn_bold': fonts+'ny-bold.otf',
        'fn_bolditalic': fonts+'ny-bold-italic.otf',
    }
]

for font in fonts:
    LabelBase.register(**font)
