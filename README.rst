.. raw:: html

   <p align="center"><img alt="Logo" src="Logo.png" width="50%" /></p>


===============================
cookiecutter-hypermodern-python
===============================

.. badges-begin

|Tests| |Read the Docs| |CalVer|

.. |Tests| image:: https://github.com/cjolowicz/cookiecutter-hypermodern-python/workflows/Tests/badge.svg
   :target: https://github.com/cjolowicz/cookiecutter-hypermodern-python/actions?workflow=Tests
.. |Read the Docs| image:: https://readthedocs.org/projects/cookiecutter-hypermodern-python/badge/
   :target: https://cookiecutter-hypermodern-python.readthedocs.io/
.. |CalVer| image:: https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg
   :target: http://calver.org/

.. badges-end

Cookiecutter_ template for a Python package based on the
`Hypermodern Python`_ article series.

✨📚✨ `Read the full documentation`__

__ https://cookiecutter-hypermodern-python.readthedocs.io/


Usage
=====

.. code:: console

   $ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python --checkout=2020.4.15.1


Features
========

.. features-begin

- Packaging and dependency management with Poetry_
- Test automation with Nox_
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
- Linting with Flake8_ and various `awesome plugins`__
- Static type-checking with mypy_ and pytype_
- Runtime type-checking with Typeguard_
- Security audit with Bandit_ and Safety_
- Git hook management with pre-commit_
- Check documentation examples with xdoctest_
- Generate API documentation with autodoc_ and napoleon_

The template supports Python 3.6, 3.7, and 3.8.

__ https://cookiecutter-hypermodern-python.readthedocs.io/en/stable/guide.html#available-linters

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

.. _`get-poetry.py`: https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py

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

1. Sign up at Codecov_.
2. Install their GitHub app.
3. Add your repository to Codecov.


Dependabot
~~~~~~~~~~

1. Sign up at Dependabot_.
2. Install their GitHub app.
3. Add your repository to Dependabot.


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

.. table-release-drafter-sections-begin

=================== ================================
Label               Section
=================== ================================
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
=================== ================================

GitHub creates the ``bug``, ``enhancement``, and ``documentation`` labels for you.
Dependabot creates the ``dependencies`` label.
Create the remaining labels on the Issues tab of your GitHub repository,
when you need them.

.. table-release-drafter-sections-end

.. quickstart-end

.. references-begin

.. _`Bandit`: https://github.com/PyCQA/bandit
.. _`Black`: https://github.com/psf/black
.. _`Click`: https://click.palletsprojects.com/
.. _`Codecov`: https://codecov.io/
.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`Coverage.py`: https://coverage.readthedocs.io/
.. _`Dependabot`: https://dependabot.com/
.. _`Flake8`: http://flake8.pycqa.org
.. _`GitHub`: https://github.com/
.. _`GitHub Actions`: https://github.com/features/actions
.. _`Hypermodern Python`: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
.. _`Nox`: https://nox.thea.codes/
.. _`Poetry`: https://python-poetry.org/
.. _`Prettier`: https://prettier.io/
.. _`PyPI`: https://pypi.org/
.. _`Read the Docs`: https://readthedocs.org/
.. _`Release Drafter`: https://github.com/release-drafter/release-drafter
.. _`Safety`: https://github.com/pyupio/safety
.. _`Sphinx`: http://www.sphinx-doc.org/
.. _`TestPyPI`: https://test.pypi.org/
.. _`Typeguard`: https://github.com/agronholm/typeguard
.. _`autodoc`: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _`mypy`: http://mypy-lang.org/
.. _`napoleon`: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
.. _`pipx`: https://pipxproject.github.io/pipx/
.. _`pre-commit`: https://pre-commit.com/
.. _`pyenv`: https://github.com/pyenv/pyenv
.. _`pytest`: https://docs.pytest.org/en/latest/
.. _`pytype`: https://google.github.io/pytype/
.. _`xdoctest`: https://github.com/Erotemic/xdoctest

.. references-end
