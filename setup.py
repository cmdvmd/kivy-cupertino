from setuptools import setup, find_packages
from kivycupertino import __version__, __author__

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='kivycupertino',
    version=__version__,
    author=__author__,
    author_email='vcmd43@gmail.com',
    license='MIT',
    description='iOS style widgets for Kivy',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/cmdvmd/kivy-cupertino',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: iOS',
        'Operating System :: MacOS',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Software Development :: Widget Sets'
    ]
)
