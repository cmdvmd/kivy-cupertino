# Kivy Cupertino Documentation

Kivy Cupertino Documentation is written with [Sphinx](https://www.sphinx-doc.org/en/master/) and
[Autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html). To improve this documentation,
[fork our repository](https://github.com/cmdvmd/kivy-cupertino/fork) and follow the instructions below

### Installing Dependencies

```shell
$ pip install sphinx
$ pip install sphinx-rtd-theme
```

### Documenting an Existing Module

To edit documentation for an existing module, update the Docstrings in the file

### Documenting a New Module

To document a new module, create a `.rst` file under [`_source/`](_source) with the same name as
the module to be documented. The following code must be included in the file:

```rst
Module
======

.. automodule:: module
   :members:
```

Then, add `_source/module` to [`index.rst`](index.rst) under `toctree` (try to keep all modules in alphabetical order).
To document your module, add Docstrings to the Python file in the following format:

```python
"""
Description of module
"""

from kivy.properties import Property

class ExampleClass:
    """
    Description of class/widget
    
    ..
       Try to include an image of the widget (.gif if animated, .png if still)

    .. image:: ../_static/widget/demo.ext
    """
    
    property = Property('default value')
    """
    Definition of property
    
    ..
       Try to include an image of the property (.gif if animated, .png if still)

    .. image:: ../_static/widget/property.ext
    
    ..
       Include examples of usage in Python and/or KV
    
    **Python**
    
      .. code-block:: python
      
         ExampleClass()
     
    **KV**
    
    .. code-block::
    
       ExampleClass:
    """
    
    def example_function(self, example_parameter):
        """
        Description of function
        
        :param example_parameter: Description of parameter
        :return: Description of return value (only if function returns a value)
        """
```

### Testing Documentation

To test written documentation, [install Sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html)
and run the following commands in [`docs/`](.):

```shell
$ make clean
$ make html
```
_Note: a [`make.bat`](make.bat) file is included under [`docs/`](.) for Windows users_

These commands will create `.html` files under `_build/html`
