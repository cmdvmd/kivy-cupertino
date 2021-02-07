from kivycupertino import fonts
from kivy.core.text import LabelBase

fonts = [
    {
        'name': 'San Francisco',
        'fn_regular': f'{fonts}sf.ttf',
        'fn_italic': f'{fonts}sf-italic.ttf',
        'fn_bold': f'{fonts}sf-bold.otf',
        'fn_bolditalic': f'{fonts}sf-bold-italic.otf',
    },
    {
        'name': 'New York',
        'fn_regular': f'{fonts}ny.ttf',
        'fn_italic': f'{fonts}ny-italic.ttf',
        'fn_bold': f'{fonts}ny-bold.otf',
        'fn_bolditalic': f'{fonts}ny-bold-italic.otf',
    }
]

for font in fonts:
    LabelBase.register(**font)
