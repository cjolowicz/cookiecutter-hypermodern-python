Hypermodern Python Cookiecutter
===============================

.. toctree::
   :hidden:
   :maxdepth: 1

   Quickstart <quickstart>
   guide
   contributing
   Code of Conduct <codeofconduct>
   license
   Changelog <https://github.com/cjolowicz/cookiecutter-hypermodern-python/releases>

.. rst-class:: badges

.. include:: ../README.md
   :parser: myst_parser.sphinx_
   :start-after: <!-- badges-begin -->
   :end-before: <!-- badges-end -->

Cookiecutter_ template for a Python package
based on the `Hypermodern Python`_ article series.


Usage
-----

.. code:: console

   $ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python \
     --checkout="2021.11.26"


Features
--------

.. include:: ../README.md
   :parser: myst_parser.sphinx_
   :start-after: <!-- features-begin -->
   :end-before: <!-- features-end -->


FAQ
---

What is this project about?
...........................

The mission of this project is to
enable current best practices
through modern Python tooling.


What makes this project different from other Python templates?
..............................................................

This is a general-purpose template for Python libraries and applications.

Our goals are:

- Focus on simplicity and minimalism
- Promote code quality through automation
- Provide reliable and repeatable processes

The project template is centered around the following tools:

- Poetry_ for packaging and dependency management
- Nox_ for automation of checks and other development tasks
- `GitHub Actions`_ for continuous integration and delivery


Why is this Python template called "hypermodern"?
.................................................

Hypermodernism_ is a school of chess that dates back to more than a century ago.
If this setup ever goes out of fashion,
I can pretend it was my secret plan from the start.
All images on the
`associated blog <Hypermodern Python_>`__ show
`past visions <Retrofuturism_>`__ of the future.

.. _Bandit: https://github.com/PyCQA/bandit
.. _Black: https://github.com/psf/black
.. _Click: https://click.palletsprojects.com/
.. _Codecov: https://codecov.io/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Coverage.py: https://coverage.readthedocs.io/
.. _Dependabot: https://dependabot.com/
.. _Flake8: http://flake8.pycqa.org
.. _GitHub Actions: https://github.com/features/actions
.. _GitHub Labeler: https://github.com/marketplace/actions/github-labeler
.. _Hypermodern Python: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
.. _Hypermodernism: https://en.wikipedia.org/wiki/Hypermodernism_(chess)
.. _MyST: https://myst-parser.readthedocs.io/
.. _Nox: https://nox.thea.codes/
.. _Poetry: https://python-poetry.org/
.. _Prettier: https://prettier.io/
.. _PyPI: https://pypi.org/
.. _Read the Docs: https://readthedocs.org/
.. _Release Drafter: https://github.com/release-drafter/release-drafter
.. _Retrofuturism: https://en.wikipedia.org/wiki/Retrofuturism
.. _Safety: https://github.com/pyupio/safety
.. _Sphinx: http://www.sphinx-doc.org/
.. _TestPyPI: https://test.pypi.org/
.. _Typeguard: https://github.com/agronholm/typeguard
.. _autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _furo: https://pradyunsg.me/furo/
.. _isort: https://pycqa.github.io/isort/
.. _mypy: http://mypy-lang.org/
.. _napoleon: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
.. _pre-commit: https://pre-commit.com/
.. _pytest: https://docs.pytest.org/en/latest/
.. _pyupgrade: https://github.com/asottile/pyupgrade
.. _sphinx-click: https://sphinx-click.readthedocs.io/
.. _xdoctest: https://github.com/Erotemic/xdoctest
