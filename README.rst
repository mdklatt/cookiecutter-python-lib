===============================
Python Library Project Template
===============================

.. _travis: https://travis-ci.org/mdklatt/cookiecutter-python-lib
.. |travis.png| image:: https://travis-ci.org/mdklatt/cookiecutter-python-lib.png?branch=master
   :alt: Travis CI build status
   :target: `travis`_

|travis.png|

.. _Cookiecutter: http://cookiecutter.readthedocs.org
.. _Python Packaging User Guide: https://packaging.python.org/en/latest/distributing.html#configuring-your-project
.. _Packaging a Python library: http://blog.ionelmc.ro/2014/05/25/python-packaging/

**Python 2.7 support is deprecated.**
**This branch is no longer actively maintained.**

This is a `Cookiecutter`_ template for creating a Python library project.

The project layout is based on the `Python Packaging User Guide`. The current
conventional wisdom forgoes the use of a source directory, but moving the 
package out of the project root provides several advantages (*cf.* 
`Packaging a Python library`_).


Template Project Features
=========================

.. _pytest: http://pytest.org
.. _Sphinx: http://sphinx-doc.org
.. _MIT License: http://choosealicense.com/licenses/mit

- Python 2.7
- `pytest`_ tests
- `Sphinx`_ documentation
- `MIT License`_


Usage
=====

.. _GitHub: https://github.com/mdklatt/cookiecutter-python-lib

Install Python requirements for using the template:

.. code-block:: console

    $ pip install --requirement=requirements.txt --user 


Create a new project directly from the template on `GitHub`_:

.. code-block:: console
   
    $ cookiecutter gh:mdklatt/cookiecutter-python-lib --checkout=py27
