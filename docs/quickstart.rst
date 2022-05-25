Quickstart Guide
================

Requirements
------------

Install Cookiecutter_:

.. code:: console

   $ pipx install cookiecutter

Install Poetry_ by downloading and running install-poetry.py_:

.. _install-poetry.py: https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py

.. code:: console

   $ python install-poetry.py

Install Nox_ and nox-poetry_:

.. code:: console

   $ pipx install nox
   $ pipx inject nox nox-poetry

pipx_ is preferred, but you can also install with ``pip install --user``.

It is recommended to set up Python 3.7, 3.8, 3.9, 3.10 using pyenv_.


Creating a project
------------------

Generate a Python project:

.. code:: console

   $ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python \
     --checkout="2021.11.26"

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

Releases are triggered by a version bump on the default branch.
It is recommended to do this in a separate pull request:

1. Switch to a branch.
2. Bump the version using `poetry version`_.
3. Commit and push to GitHub.
4. Open a pull request.
5. Merge the pull request.

.. _poetry version: https://python-poetry.org/docs/cli/#version

The Release workflow performs the following automated steps:

- Build and upload the package to PyPI.
- Apply a version tag to the repository.
- Publish a GitHub Release.

Release notes are populated with the titles and authors of merged pull requests.
You can group the pull requests into separate sections
by applying labels to them, like this:

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

.. table-release-drafter-sections-end

.. _Bandit: https://github.com/PyCQA/bandit
.. _Black: https://github.com/psf/black
.. _Click: https://click.palletsprojects.com/
.. _Codecov: https://codecov.io/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Coverage.py: https://coverage.readthedocs.io/
.. _Dependabot: https://dependabot.com/
.. _Flake8: http://flake8.pycqa.org
.. _GitHub Actions: https://github.com/features/actions
.. _Hypermodern Python: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
.. _isort: https://pycqa.github.io/isort/
.. _MyST: https://myst-parser.readthedocs.io/
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
.. _furo: https://pradyunsg.me/furo/
.. _mypy: http://mypy-lang.org/
.. _napoleon: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
.. _pre-commit: https://pre-commit.com/
.. _pytest: https://docs.pytest.org/en/latest/
.. _pyupgrade: https://github.com/asottile/pyupgrade
.. _sphinx-click: https://sphinx-click.readthedocs.io/
.. _xdoctest: https://github.com/Erotemic/xdoctest
.. _GitHub Labeler: https://github.com/marketplace/actions/github-labeler

.. quickstart-references-begin

.. _GitHub: https://github.com/
.. _nox-poetry: https://nox-poetry.readthedocs.io/
.. _pipx: https://pipxproject.github.io/pipx/
.. _pyenv: https://github.com/pyenv/pyenv

.. quickstart-references-end
