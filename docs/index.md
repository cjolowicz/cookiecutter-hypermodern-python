# Hypermodern Python Cookiecutter

```{toctree}
:hidden: true
:maxdepth: 1

Quickstart <quickstart>
guide
contributing
Code of Conduct <codeofconduct>
license
Changelog <https://github.com/cjolowicz/cookiecutter-hypermodern-python/releases>
```

```{eval-rst}
.. rst-class:: badges
```

```{eval-rst}
.. include:: ../README.md
   :parser: myst_parser.sphinx_
   :start-after: <!-- badges-begin -->
   :end-before: <!-- badges-end -->
```

[Cookiecutter] template for a Python package
based on the [Hypermodern Python] article series.

## Usage

```console
$ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python \
  --checkout="2021.11.26"
```

## Features

```{eval-rst}
.. include:: ../README.md
   :parser: myst_parser.sphinx_
   :start-after: <!-- features-begin -->
   :end-before: <!-- features-end -->

```

## FAQ

### What is this project about?

The mission of this project is to
enable current best practices
through modern Python tooling.

### What makes this project different from other Python templates?

This is a general-purpose template for Python libraries and applications.

Our goals are:

- Focus on simplicity and minimalism
- Promote code quality through automation
- Provide reliable and repeatable processes

The project template is centered around the following tools:

- [Poetry] for packaging and dependency management
- [Nox] for automation of checks and other development tasks
- [GitHub Actions] for continuous integration and delivery

### Why is this Python template called "hypermodern"?

[Hypermodernism] is a school of chess that dates back to more than a century ago.
If this setup ever goes out of fashion,
I can pretend it was my secret plan from the start.
All images on the
[associated blog][hypermodern python] show
[past visions][retrofuturism] of the future.

[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[bandit]: https://github.com/PyCQA/bandit
[black]: https://github.com/psf/black
[click]: https://click.palletsprojects.com/
[codecov]: https://codecov.io/
[cookiecutter]: https://github.com/audreyr/cookiecutter
[coverage.py]: https://coverage.readthedocs.io/
[dependabot]: https://dependabot.com/
[flake8]: http://flake8.pycqa.org
[furo]: https://pradyunsg.me/furo/
[github actions]: https://github.com/features/actions
[github labeler]: https://github.com/marketplace/actions/github-labeler
[hypermodern python]: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
[hypermodernism]: https://en.wikipedia.org/wiki/Hypermodernism_(chess)
[isort]: https://pycqa.github.io/isort/
[mypy]: http://mypy-lang.org/
[myst]: https://myst-parser.readthedocs.io/
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[nox]: https://nox.thea.codes/
[poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/
[prettier]: https://prettier.io/
[pypi]: https://pypi.org/
[pytest]: https://docs.pytest.org/en/latest/
[pyupgrade]: https://github.com/asottile/pyupgrade
[read the docs]: https://readthedocs.org/
[release drafter]: https://github.com/release-drafter/release-drafter
[retrofuturism]: https://en.wikipedia.org/wiki/Retrofuturism
[safety]: https://github.com/pyupio/safety
[sphinx]: http://www.sphinx-doc.org/
[sphinx-click]: https://sphinx-click.readthedocs.io/
[testpypi]: https://test.pypi.org/
[typeguard]: https://github.com/agronholm/typeguard
[xdoctest]: https://github.com/Erotemic/xdoctest
