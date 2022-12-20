"""
A program to initialize Kivy Cupertino
"""

import os
from kivy.logger import Logger

__author__ = 'cmdvmd'
__copyright__ = '2021, cmdvmd'
__version__ = '0.1.1b0'
__license__ = 'MIT'

root_path = os.path.dirname(__file__) + '/'
fonts_path = os.path.join(root_path, 'fonts/')
sf_path = os.path.join(fonts_path, 'San Francisco/')
ny_path = os.path.join(fonts_path, 'New York/')

from .init import fonts, widgets

Logger.info(f'Kivy Cupertino: Version {__version__}')
Logger.info(f'Kivy Cupertino: Installed at "{__file__}"')
