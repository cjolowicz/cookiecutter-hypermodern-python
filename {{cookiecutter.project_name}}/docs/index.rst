{{cookiecutter.friendly_name}}
==============================

.. toctree::
   :hidden:
   :maxdepth: 1

   reference
   contributing
   Code of Conduct <codeofconduct>
   license
   Changelog <https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/releases>

.. include:: ../README.rst
   :start-after: badges-begin
   :end-before: badges-end

This package has a command-line interface.


Installation
------------

To install {{cookiecutter.friendly_name}},
run this command in your terminal:

.. code-block:: console

   $ pip install {{cookiecutter.project_name}}


Usage
-----

{{cookiecutter.friendly_name}}'s usage looks like:

.. code-block:: console

   $ {{cookiecutter.project_name}} [OPTIONS]

.. option:: --version

   Display the version and exit.

.. option:: --help

   Display a short usage message and exit.
