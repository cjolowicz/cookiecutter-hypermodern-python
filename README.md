<p align="center"><img alt="Logo" src="Logo.png" width="50%" /></p>

# cookiecutter-hypermodern-python

[![Tests](https://github.com/cjolowicz/cookiecutter-hypermodern-python/workflows/Tests/badge.svg)][tests]
[![Read the Docs](https://readthedocs.org/projects/cookiecutter-hypermodern-python/badge/)][docs]
[![calver YYYY.MM.DD](https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg)][calver]

[Cookiecutter] template for a Python package based on the
[Hypermodern Python] article series.

:books: [Read the full documentation][docs]

[tests]: https://github.com/cjolowicz/cookiecutter-hypermodern-python/actions?workflow=Tests
[docs]: https://cookiecutter-hypermodern-python.readthedocs.io/
[calver]: http://calver.org/
[cookiecutter]: https://github.com/audreyr/cookiecutter
[hypermodern python]: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769

## Usage

```console
$ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python --checkout=2020.4.15.1
```

## Features

- Packaging and dependency management with [Poetry]
- Test automation with [Nox]
- Continuous integration with [GitHub Actions]
- Documentation with [Sphinx] and [Read the Docs]
- Automated uploads to [PyPI] and [TestPyPI]
- Automated release notes with [Release Drafter]
- Code formatting with [Black] and [Prettier]
- Testing with [Pytest]
- Code coverage with [Coverage.py]
- Coverage reporting with [Codecov]
- Command-line interface with [Click]
- Linting with [Flake8] and various awesome plugins
- Static type-checking with [mypy] and [pytype]
- Runtime type-checking with [Typeguard]
- Security audit with [Bandit] and [Safety]
- Git hook management with [pre-commit]
- Check documentation examples with [xdoctest]
- Generate API documentation with [autodoc], [napoleon], and [sphinx-autodoc-typehints]

The template supports Python 3.6, 3.7, and 3.8.

[poetry]: https://python-poetry.org/
[nox]: https://nox.thea.codes/
[github actions]: https://github.com/features/actions
[sphinx]: http://www.sphinx-doc.org/
[read the docs]: https://readthedocs.org/
[pypi]: https://pypi.org/
[testpypi]: https://test.pypi.org
[release drafter]: https://github.com/release-drafter/release-drafter
[black]: https://github.com/psf/black
[prettier]: https://github.com/prettier/prettier
[pytest]: https://docs.pytest.org/en/latest/
[coverage.py]: https://coverage.readthedocs.io/
[codecov]: https://codecov.io/
[click]: https://click.palletsprojects.com/
[flake8]: http://flake8.pycqa.org
[mypy]: http://mypy-lang.org/
[pytype]: https://google.github.io/pytype/
[typeguard]: https://github.com/agronholm/typeguard
[bandit]: https://github.com/PyCQA/bandit
[safety]: https://github.com/pyupio/safety
[pre-commit]: https://pre-commit.com/
[xdoctest]: https://github.com/Erotemic/xdoctest
[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[sphinx-autodoc-typehints]: https://github.com/agronholm/sphinx-autodoc-typehints

## Quickstart

### Requirements

Install Cookiecutter:

```console
$ pipx install cookiecutter
```

Install Poetry:

```console
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

Install Nox:

```console
$ pipx install nox
```

[pipx] is preferred, but you can also install with `pip install --user`.

It is recommended to set up Python 3.6, 3.7, and 3.8 using [pyenv].

[pipx]: https://github.com/pipxproject/pipx
[pyenv]: https://github.com/pyenv/pyenv

### Creating a project

Generate a Python project:

```console
$ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python --checkout=2020.4.15.1
```

Change to the root directory of your new project,
and create a Git repository:

```console
$ git init
$ git add .
$ git commit
```

### Local testing

Run the full test suite:

```console
$ nox
```

List the available Nox sessions:

```console
$ nox --list-sessions
```

### Continuous Integration

#### GitHub

1. Create an empty repository for your project.
2. Follow the instructions to push an existing repository from the command line.

#### PyPI

1. Sign up at [PyPI].
2. Go to the Account Settings on PyPI,
   generate an API token, and copy it.
3. Go to the repository settings on GitHub, and
   add a secret named `PYPI_TOKEN` with the token you just copied.

[pypi]: https://pypi.org/

#### TestPyPI

1. Sign up at [TestPyPI].
2. Go to the Account Settings on TestPyPI,
   generate an API token, and copy it.
3. Go to the repository settings on GitHub, and
   add a secret named `TEST_PYPI_TOKEN` with the token you just copied.

[testpypi]: https://test.pypi.org/

#### Codecov

1. Sign up at [Codecov], and install their GitHub app.
2. Add your repository to Codecov.

[codecov]: https://codecov.io/

#### Read the Docs

1. Sign up at [Read the Docs].
2. Import your GitHub repository, using the button _Import a Project_.

[read the docs]: https://readthedocs.org/

### Releasing

1. Bump the version using `poetry version`. Push to GitHub.
2. Publish a GitHub Release.
3. GitHub Action triggers the PyPI upload.

Release notes are pre-filled with titles and authors of merged pull requests.

Use labels to group the pull requests into sections:

| Label           | Section                                      |
| --------------- | -------------------------------------------- |
| `breaking`      | :boom: Breaking Changes                      |
| `bug`           | :beetle: Fixes                               |
| `dependencies`  | :package: Dependencies                       |
| `ci`            | :construction_worker: Continuous Integration |
| `documentation` | :books: Documentation                        |
| `enhancement`   | :rocket: Features                            |
| `performance`   | :racehorse: Performance                      |
| `refactoring`   | :hammer: Refactoring                         |
| `removal`       | :fire: Removals and Deprecations             |
| `style`         | :lipstick: Style                             |
| `testing`       | :rotating_light: Testing                     |

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you.
Create the remaining labels on the Issues tab of your GitHub repository.
