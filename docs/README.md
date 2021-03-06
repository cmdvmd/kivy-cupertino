# Kivy Cupertino Documentation

Kivy Cupertino Documentation is written with [Sphinx](https://www.sphinx-doc.org/en/master/) and
[Autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html). To improve this documentation,
[fork this repository](https://github.com/cmdvmd/kivy-cupertino/fork) and follow the instructions below

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

from kivy.properties import NumericProperty

class ExampleClass:
    """
    Description of class/widget
    
    ..
       Try to include an image of the widget (.gif if animated, .png if still)

    .. image:: ../_static/widget.ext
    """
    
    example_property = NumericProperty(0)
    """
    Description of property
    
    ..
       Include the type and default value of the property

    :attr:`example_property` is a :class:`~kivy.properties.NumericProperty` and defaults to `0`
    """
    
    def example_function(self, example_parameter):
        """
        Description of function
        
        :param example_parameter: Description of parameter
        :return: Description of return value (only if function returns a value)
        """
```

### Testing Documentation

To test written documentation, navigate to [`docs/`](.) and run the following commands:

```shell
make clean
make html
```
_Note: a [`make.bat`](make.bat) file is included under [`docs/`](.) for Windows users_

These commands will create `.html` files under `_build/html`
