{% set delim = "=" * cookiecutter.lib_name|length %}
{{ delim }}
{{ cookiecutter.lib_name }}
{{ delim }}

This is the {{ cookiecutter.lib_name }} library.


Minimum Requirements
====================

- Python 2.7


Optional Requirements
=====================

.. _pytest: http://pytest.org
.. _Sphinx: http://sphinx-doc.org

- `pytest`_ (for running the test suite)
- `Sphinx`_ (for generating documentation)


Basic Setup
===========

Install for the current user:

.. code-block:: console

    $ python setup.py install --user


Run the test suite:

.. code-block:: console
   
    $ pytest test/


Build documentation:

.. code-block:: console

    $ sphinx-build -b html doc doc/_build/html
