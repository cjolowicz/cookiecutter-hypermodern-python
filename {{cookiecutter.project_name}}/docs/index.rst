The Hypermodern Python Project
==============================

.. toctree::
   :hidden:
   :maxdepth: 1

   license
   reference

The example project for the
`Hypermodern Python <https://medium.com/@cjolowicz/{{cookiecutter.project_name}}-d44485d9d769>`_
article series.
The command-line interface prints random facts to your console,
using the `Wikipedia API <https://en.wikipedia.org/api/rest_v1/#/>`_.


Installation
------------

To install the Hypermodern Python project,
run this command in your terminal:

.. code-block:: console

   $ pip install {{cookiecutter.project_name}}


Usage
-----

Hypermodern Python's usage looks like:

.. code-block:: console

   $ {{cookiecutter.project_name}} [OPTIONS]

.. option:: -l <language>, --language <language>

   The Wikipedia language edition,
   as identified by its subdomain on
   `wikipedia.org <https://www.wikipedia.org/>`_.
   By default, the English Wikipedia is selected.

.. option:: --version

   Display the version and exit.

.. option:: --help

   Display a short usage message and exit.
