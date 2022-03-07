import setuptools

with open('README.md', encoding='utf-8') as readme:
    long_description = readme.read()

setuptools.setup(
    name='kivycupertino',
    version='0.1.1b0',
    author='cmdvmd',
    author_email='vcmd43@gmail.com',
    license='MIT',
    description='iOS style widgets for Kivy',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cmdvmd/kivy-cupertino',
    python_requires='>=3.7',
    keywords='kivy widget iOS',
    packages=[
        'kivycupertino'
    ],
    install_requires=[
        'kivy>=2.1.0'
    ],
    extras_require={
        'dev': [
            'sphinx>=4.4.0',
            'sphinx-rtd-theme>=1.0.0'
        ]
    },
    project_urls={
        'Documentation': 'https://kivy-cupertino.rtfd.io'
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Software Development :: Widget Sets'
    ],
)
