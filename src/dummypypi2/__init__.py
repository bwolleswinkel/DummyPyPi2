"""
DummyPyPi2
==========

Provides
  1. Some random functionalities for demonstration purposes
  2. A submodule `control` as a demonstration of package structure
  3. Global configuration management via the `_config` submodule (accessible through non-private functions in the main module)

How to use the documentation
----------------------------
Documentation is available in two forms: docstrings provided with the code (should be everywhere!), and a 'ReadTheDocs' hosted version with more elaborate explanations and examples on the DummyPyPi2 `homepage <https://dummypypi2.readthedocs.io/en/latest/>`_.

The docstring examples assume that `dummypypi2` has been imported as ``dp``::
>>> import dummypypi2 as dp

Code snippets are indicated by three greater-than signs:
>>> x = 42
>>> x = x + 1

Use the built-in ``help`` function to view a function's docstring:
>>> help(dp.get_signed_angle)
... # doctest: +SKIP

Available sub-packages
----------------------
control
    Does nothing at the moment

Utilities
---------
__version__
    DummyPyPi2 version string

"""

from .utils import *

from . import control

from ._version import __version__
from ._config.algo import algo_options, set_algo_options
from ._config.plot import set_display_options