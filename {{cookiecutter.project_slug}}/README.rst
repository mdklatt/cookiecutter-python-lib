{% set delim = "=" * cookiecutter.lib_name|length -%}
{{ delim }}
{{ cookiecutter.lib_name }}
{{ delim }}

Python library created from the `mdklatt/cookiecutter-python-lib`_ template.
Python 3.8+ is required.


Basic Setup
===========

Install for the current user:

.. code-block:: console

    $ python -m pip install -e ".[dev]"


Run the test suite:

.. code-block:: console
   
    $ python -m pytest test/


Build documentation:

.. code-block:: console

    $ python -m sphinx -b html doc doc/_build/html


.. _mdklatt/cookiecutter-python-lib: https://github.com/mdklatt/cookiecutter-python-lib