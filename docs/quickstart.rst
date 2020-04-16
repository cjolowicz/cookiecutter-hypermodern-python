Quickstart Guide
================

Requirements
------------

Install Cookiecutter_:

.. code:: console

   $ pipx install cookiecutter

Install Poetry_ by downloading and running get-poetry.py_:

.. _`get-poetry.py`: https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py

.. code:: console

   $ python get-poetry.py

Install Nox_:

.. code:: console

   $ pipx install nox

pipx_ is preferred,
but you can also install with ``pip install --user``.

It is recommended to set up Python 3.6, 3.7, and 3.8 using pyenv_.


Creating a project
------------------

Generate a Python project:

.. code:: console

   $ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python \
     --checkout="2020.4.15.1"

Change to the root directory of your new project,
and create a Git repository:

.. code:: console

   $ git init
   $ git add .
   $ git commit

Local testing
-------------

Run the full test suite:

.. code:: console

   $ nox

List the available Nox sessions:

.. code:: console

   $ nox --list-sessions


Continuous Integration
----------------------

GitHub
~~~~~~

1. Sign up at GitHub_.
2. Create an empty repository for your project.
3. Follow the instructions to push an existing repository from the command line.


PyPI
~~~~

1. Sign up at PyPI_.
2. Go to the Account Settings on PyPI,
   generate an API token, and copy it.
3. Go to the repository settings on GitHub, and
   add a secret named ``PYPI_TOKEN`` with the token you just copied.


TestPyPI
~~~~~~~~

1. Sign up at TestPyPI_.
2. Go to the Account Settings on TestPyPI,
   generate an API token, and copy it.
3. Go to the repository settings on GitHub, and
   add a secret named ``TEST_PYPI_TOKEN`` with the token you just copied.


Codecov
~~~~~~~

1. Sign up at Codecov_, and install their GitHub app.
2. Add your repository to Codecov.


Dependabot
~~~~~~~~~~

1. Sign up at Dependabot_, and install their GitHub app.
2. Add your repository to Dependabot.


Read the Docs
~~~~~~~~~~~~~

1. Sign up at `Read the Docs`_.
2. Import your GitHub repository, using the button *Import a Project*.


Releasing
---------

1. Bump the version using `poetry version`_. Push to GitHub.
2. Publish a GitHub Release.
3. GitHub Action triggers the PyPI upload.

.. _`poetry version`: https://python-poetry.org/docs/cli/#version

Release notes are pre-filled with titles and authors of merged pull requests.

Use labels to group the pull requests into sections:

.. include:: guide.rst
   :start-after: table-release-drafter-sections-begin
   :end-before: table-release-drafter-sections-end

GitHub creates the ``bug``, ``enhancement``, and ``documentation`` labels for you.
Create the remaining labels on the Issues tab of your GitHub repository.


Caveats
-------

When upgrading Sphinx or its extensions using Poetry,
also update the requirements located in ``docs/requirements.txt`` for Read the Docs.

.. include:: guide.rst
   :start-after: references-begin
   :end-before: references-end
