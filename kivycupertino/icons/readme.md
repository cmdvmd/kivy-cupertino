**San Francisco Symbols**

<h6>Note: This is not officially supported. Please use at your own risk</h6>

Basic Usage

```python
from kivy.core.text import LabelBase
from kivy.base import runTouchApp
from kivy.lang.builder import Builder

LabelBase.register(name='sf', fn_regular='sficonsets.ttf')

runTouchApp(Builder.load_string("""
Button:
    font_name: 'sf'
    text: '\ue7b8'
"""))
``` 

The above code shows the ```Alarm``` San Francisco Symbol

| Icon | Hexcode |
|------|---------|
|Airplane|0xed19|
|Alarm|0xe7ba|
|Arrow Clockwise|0xe7ce|
|Arrow Counterclockwise|0xe7d2|
|Arrow Left|0xe7ed|
|Arrow Right|0xe800|
|Cellular|0xe7c0|
|Info Circle|0xe9e8|
|Maximize|0xe816|
|Minimize|0xe7de|

There are more Icons to come so stay on the look out


