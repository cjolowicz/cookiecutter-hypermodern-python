===============================
cookiecutter-hypermodern-python
===============================

.. badges-begin

| |Status| |Python Version| |CalVer| |License|
| |Read the Docs| |Tests| |Codecov|
| |pre-commit| |Black|

.. |Status| image:: https://badgen.net/badge/status/alpha/d8624d
   :target: https://badgen.net/badge/status/alpha/d8624d
   :alt: Project Status
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/cookiecutter-hypermodern-python-instance
   :target: https://github.com/cjolowicz/cookiecutter-hypermodern-python
   :alt: Python Version
.. |CalVer| image:: https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg
   :target: http://calver.org/
   :alt: CalVer
.. |License| image:: https://img.shields.io/github/license/cjolowicz/cookiecutter-hypermodern-python
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/cookiecutter-hypermodern-python/latest.svg?label=Read%20the%20Docs
   :target: https://cookiecutter-hypermodern-python.readthedocs.io/
   :alt: Read the documentation at https://cookiecutter-hypermodern-python.readthedocs.io/
.. |Tests| image:: https://github.com/cjolowicz/cookiecutter-hypermodern-python/workflows/Tests/badge.svg
   :target: https://github.com/cjolowicz/cookiecutter-hypermodern-python/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/cjolowicz/cookiecutter-hypermodern-python-instance/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/cjolowicz/cookiecutter-hypermodern-python-instance
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black

.. badges-end

|

.. raw:: html

   <p align="center"><img alt="logo" src="docs/_static/logo.png" width="50%" /></p>


Cookiecutter_ template for a Python package based on the
`Hypermodern Python`_ article series.

✨📚✨ `Read the full documentation`__

__ https://cookiecutter-hypermodern-python.readthedocs.io/


Usage
=====

.. code:: console

   $ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python --checkout=2021.11.26


Features
========

.. features-begin

- Packaging and dependency management with Poetry_
- Test automation with Nox_
- Linting with pre-commit_ and Flake8_
- Continuous integration with `GitHub Actions`_
- Documentation with Sphinx_ and `Read the Docs`_ using the furo_ theme
- Automated uploads to PyPI_ and TestPyPI_
- Automated release notes with `Release Drafter`_
- Automated dependency updates with Dependabot_
- Code formatting with Black_ and Prettier_
- Import sorting with isort_
- Testing with pytest_
- Code coverage with Coverage.py_
- Coverage reporting with Codecov_
- Command-line interface with Click_
- Static type-checking with mypy_
- Runtime type-checking with Typeguard_
- Automated Python syntax upgrades with pyupgrade_
- Security audit with Bandit_ and Safety_
- Check documentation examples with xdoctest_
- Generate API documentation with autodoc_ and napoleon_
- Generate command-line reference with sphinx-click_
- Manage project labels with `GitHub Labeler`_

The template supports Python 3.7, 3.8, 3.9, and 3.10.

.. features-end

.. references-begin

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

.. references-end
