import kivycupertino
import setuptools

with open('README.md', encoding='utf-8') as readme:
    long_description = readme.read()

setuptools.setup(
    name='kivycupertino',
    version=kivycupertino.__version__,
    author=kivycupertino.__author__,
    author_email='vcmd43@gmail.com',
    license=kivycupertino.__license__,
    description='iOS style widgets for Kivy',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cmdvmd/kivy-cupertino',
    project_urls={
        'Documentation': 'https://kivy-cupertino.rtfd.io'
    },
    install_requires=[
        'kivy'
    ],
    packages=[
        'kivycupertino'
    ],
    package_data={
        'kivycupertino': [
            'fonts/*',
            'icons/*',
            'images/*',
            'init/*',
            'uix/*'
        ]
    },
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
