.. raw:: html

   <p align="center"><img alt="Logo" src="Logo.png" width="50%" /></p>


===============================
cookiecutter-hypermodern-python
===============================

.. badges-begin

|Tests| |Read the Docs| |CalVer| |Codecov| |Python Version| |License| |Black| |pre-commit| |Dependabot|

.. |Tests| image:: https://github.com/cjolowicz/cookiecutter-hypermodern-python/workflows/Tests/badge.svg
   :target: https://github.com/cjolowicz/cookiecutter-hypermodern-python/actions?workflow=Tests
   :alt: Tests
.. |Read the Docs| image:: https://readthedocs.org/projects/cookiecutter-hypermodern-python/badge/
   :target: https://cookiecutter-hypermodern-python.readthedocs.io/
   :alt: Read the Docs
.. |CalVer| image:: https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg
   :target: http://calver.org/
   :alt: CalVer
.. |Codecov| image:: https://codecov.io/gh/cjolowicz/cookiecutter-hypermodern-python-instance/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/cjolowicz/cookiecutter-hypermodern-python-instance
   :alt: Codecov
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/cookiecutter-hypermodern-python-instance
   :target: https://github.com/cjolowicz/cookiecutter-hypermodern-python
   :alt: Python Version
.. |License| image:: https://img.shields.io/github/license/cjolowicz/cookiecutter-hypermodern-python
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Dependabot| image:: https://api.dependabot.com/badges/status?host=github&repo=cjolowicz/cookiecutter-hypermodern-python-instance
   :target: https://dependabot.com
   :alt: Dependabot

.. badges-end

Cookiecutter_ template for a Python package based on the
`Hypermodern Python`_ article series.

✨📚✨ `Read the full documentation`__

__ https://cookiecutter-hypermodern-python.readthedocs.io/


Usage
=====

.. code:: console

   $ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python --checkout=2020.5.15


Features
========

.. features-begin

- Packaging and dependency management with Poetry_
- Test automation with Nox_
- Linting with pre-commit_ and Flake8_
- Continuous integration with `GitHub Actions`_
- Documentation with Sphinx_ and `Read the Docs`_
- Automated uploads to PyPI_ and TestPyPI_
- Automated release notes with `Release Drafter`_
- Automated dependency updates with Dependabot_
- Code formatting with Black_ and Prettier_
- Testing with pytest_
- Code coverage with Coverage.py_
- Coverage reporting with Codecov_
- Command-line interface with Click_
- Static type-checking with mypy_
- Runtime type-checking with Typeguard_
- Security audit with Bandit_ and Safety_
- Check documentation examples with xdoctest_
- Generate API documentation with autodoc_ and napoleon_

The template supports Python 3.6, 3.7, and 3.8.

.. features-end


Quickstart
==========

.. quickstart-begin

Requirements
------------

Install Cookiecutter_:

.. code:: console

   $ pipx install cookiecutter

Install Poetry_ by downloading and running get-poetry.py_:

.. _get-poetry.py: https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py

.. code:: console

   $ python get-poetry.py

Install Nox_:

.. code:: console

   $ pipx install nox

pipx_ is preferred, but you can also install with ``pip install --user``.

It is recommended to set up Python 3.6, 3.7, and 3.8 using pyenv_.


Creating a project
------------------

Generate a Python project:

.. code:: console

   $ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python \
     --checkout="2020.5.15"

Change to the root directory of your new project,
and create a Git repository:

.. code:: console

   $ git init
   $ git add .
   $ git commit


Running
-------

Run the command-line interface from the source tree:

.. code:: console

   $ poetry install
   $ poetry run <project>

Run an interactive Python session:

.. code:: console

   $ poetry install
   $ poetry run python


Testing
-------

Run the full test suite:

.. code:: console

   $ nox

List the available Nox sessions:

.. code:: console

   $ nox --list-sessions

Install the pre-commit hooks:

.. code:: console

   $ nox -s pre-commit -- install


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

1. Sign up at Codecov_.
2. Install their GitHub app.


Dependabot
~~~~~~~~~~

1. Sign up at Dependabot_.
2. Install their GitHub app.


Read the Docs
~~~~~~~~~~~~~

1. Sign up at `Read the Docs`_.
2. Import your GitHub repository, using the button *Import a Project*.
3. Install the GitHub webhook,
   using the button *Add integration*
   on the *Integrations* tab
   in the *Admin* section of your project
   on Read the Docs.


Releasing
---------

1. Bump the version using `poetry version`_. Push to GitHub.
2. Publish a GitHub Release.
3. GitHub Action triggers the PyPI upload.

.. _poetry version: https://python-poetry.org/docs/cli/#version

Release notes are pre-filled with titles and authors of merged pull requests.

Use labels to group the pull requests into sections:

.. table-release-drafter-sections-begin

.. table::
   :class: hypermodern-table
   :widths: auto

   =================== ============================
   Pull Request Label  Section in Release Notes
   =================== ============================
   ``breaking``        💥 Breaking Changes
   ``enhancement``     🚀 Features
   ``removal``         🔥 Removals and Deprecations
   ``bug``             🐞 Fixes
   ``performance``     🐎 Performance
   ``testing``         🚨 Testing
   ``ci``              👷 Continuous Integration
   ``documentation``   📚 Documentation
   ``refactoring``     🔨 Refactoring
   ``style``           💄 Style
   ``dependencies``    📦 Dependencies
   =================== ============================

GitHub creates the ``bug``, ``enhancement``, and ``documentation`` labels for you.
Dependabot creates the ``dependencies`` label.
Create the remaining labels on the *Issues* tab of your GitHub repository,
when you need them.

.. table-release-drafter-sections-end

.. quickstart-end

.. references-begin

.. _Bandit: https://github.com/PyCQA/bandit
.. _Black: https://github.com/psf/black
.. _Click: https://click.palletsprojects.com/
.. _Codecov: https://codecov.io/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Coverage.py: https://coverage.readthedocs.io/
.. _Dependabot: https://dependabot.com/
.. _Flake8: http://flake8.pycqa.org
.. _GitHub: https://github.com/
.. _GitHub Actions: https://github.com/features/actions
.. _Hypermodern Python: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
.. _Nox: https://nox.thea.codes/
.. _Poetry: https://python-poetry.org/
.. _Prettier: https://prettier.io/
.. _PyPI: https://pypi.org/
.. _Read the Docs: https://readthedocs.org/
.. _Release Drafter: https://github.com/release-drafter/release-drafter
.. _Safety: https://github.com/pyupio/safety
.. _Sphinx: http://www.sphinx-doc.org/
.. _TestPyPI: https://test.pypi.org/
.. _Typeguard: https://github.com/agronholm/typeguard
.. _autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _mypy: http://mypy-lang.org/
.. _napoleon: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
.. _pipx: https://pipxproject.github.io/pipx/
.. _pre-commit: https://pre-commit.com/
.. _pyenv: https://github.com/pyenv/pyenv
.. _pytest: https://docs.pytest.org/en/latest/
.. _xdoctest: https://github.com/Erotemic/xdoctest

.. references-end
