<p align="center"><img alt="Logo" src="Logo.png" width="50%" /></p>

# cookiecutter-hypermodern-python

[![Tests](https://github.com/cjolowicz/cookiecutter-hypermodern-python/workflows/Tests/badge.svg)](https://github.com/cjolowicz/cookiecutter-hypermodern-python/actions?workflow=Tests)
[![calver YYYY.MM.DD](https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg)](http://calver.org/)

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for a
Python package based on the
[Hypermodern Python](https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769)
article series.

## Usage

```sh
cookiecutter \
    https://github.com/cjolowicz/cookiecutter-hypermodern-python \
    --checkout=2020.3.27
```

## Features

- Packaging and dependency management with [Poetry](https://python-poetry.org/)
- Test automation with [Nox](https://nox.thea.codes/)
- Continuous integration with [GitHub Actions](https://github.com/features/actions)
- Documentation with [Sphinx](http://www.sphinx-doc.org/) and [Read the Docs](https://readthedocs.org/)
- Automated uploads to [PyPI](https://pypi.org/) and [TestPyPI](https://test.pypi.org)
- Automated release notes with [Release Drafter](https://github.com/release-drafter/release-drafter)
- Code formatting with [Black](https://github.com/psf/black) and [Prettier](https://github.com/prettier/prettier)
- Testing with [Pytest](https://docs.pytest.org/en/latest/)
- Code coverage with [Coverage.py](https://coverage.readthedocs.io/)
- Coverage reporting with [Codecov](https://codecov.io/)
- Command-line interface with [Click](https://click.palletsprojects.com/)
- Linting with [Flake8](http://flake8.pycqa.org) and various awesome plugins
- Static type-checking with [mypy](http://mypy-lang.org/) and [pytype](https://google.github.io/pytype/)
- Runtime type-checking with [Typeguard](https://github.com/agronholm/typeguard)
- Security audit with [Bandit](https://github.com/PyCQA/bandit) and [Safety](https://github.com/pyupio/safety)
- Git hook management with [pre-commit](https://pre-commit.com/)
- Check documentation examples with [xdoctest](https://github.com/Erotemic/xdoctest)
- Generate API documentation with
  [autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html),
  [napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html), and
  [sphinx-autodoc-typehints](https://github.com/agronholm/sphinx-autodoc-typehints)

The template supports Python 3.6, 3.7, and 3.8.

## Quickstart

### Requirements

Install Cookiecutter:

```sh
pipx install cookiecutter
```

Install Poetry:

```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

Install Nox:

```sh
pipx install nox
```

[pipx](https://github.com/pipxproject/pipx) is preferred,
but you can also install with `pip install --user`.

It is recommended to set up Python 3.6, 3.7, and 3.8
using [pyenv](https://github.com/pyenv/pyenv).

### Creating a project

Generate a Python project:

```sh
cookiecutter \
   https://github.com/cjolowicz/cookiecutter-hypermodern-python \
   --checkout=2020.3.27
```

Change to the root directory of your new project,
and create a Git repository:

```sh
git init
git add .
git commit
```

### Local testing

Run the full test suite:

```sh
nox
```

List the available Nox sessions:

```sh
nox --list-sessions
```

### Continuous Integration

#### GitHub

1. Create an empty repository for your project.
2. Follow the instructions to push an existing repository from the command line.

#### PyPI

1. Sign up at [PyPI](https://pypi.org/).
2. Go to the Account Settings on PyPI,
   generate an API token, and copy it.
3. Go to the repository settings on GitHub, and
   add a secret named `PYPI_TOKEN` with the token you just copied.

#### TestPyPI

1. Sign up at [TestPyPI](https://test.pypi.org/).
2. Go to the Account Settings on TestPyPI,
   generate an API token, and copy it.
3. Go to the repository settings on GitHub, and
   add a secret named `TEST_PYPI_TOKEN` with the token you just copied.

#### Codecov

1. Sign up at [Codecov](https://codecov.io/), and install their GitHub app.
2. Add your repository to Codecov.

#### Read the Docs

1. Sign up at [Read the Docs](https://readthedocs.org/).
2. Import your GitHub repository, using the button _Import a Project_.

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
| `build`         | :package: Build System and Dependencies      |
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

## Caveats

When upgrading Sphinx or its extensions using Poetry,
also update the requirements located in
[docs/requirements.txt]({{cookiecutter.project_name}}/docs/requirements.txt)
for Read the Docs.

## Guide

The project setup is described in detail in the
[Hypermodern Python](https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769) article series:

- [Chapter 1: Setup](https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769)
- [Chapter 2: Testing](https://medium.com/@cjolowicz/hypermodern-python-2-testing-ae907a920260)
- [Chapter 3: Linting](https://medium.com/@cjolowicz/hypermodern-python-3-linting-e2f15708da80)
- [Chapter 4: Typing](https://medium.com/@cjolowicz/hypermodern-python-4-typing-31bcf12314ff)
- [Chapter 5: Documentation](https://medium.com/@cjolowicz/hypermodern-python-5-documentation-13219991028c)
- [Chapter 6: CI/CD](https://medium.com/@cjolowicz/hypermodern-python-6-ci-cd-b233accfa2f6)

You can also read the articles on my [blog](https://cjolowicz.github.io/).
