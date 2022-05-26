---
substitutions:
  HPC: "*Hypermodern Python Cookiecutter*"
---

<!--
TODO

- turn inline links into reference links
- fix section references
- convert tables to native Markdown
- check that {{ HPC }} works inside admonitions

-->

# User Guide

This is the user guide
for the [Hypermodern Python Cookiecutter],
a Python template based on the [Hypermodern Python] article series.

If you're in a hurry, check out the {doc}`quickstart guide <quickstart>`
and the {ref}`tutorials <Tutorials>`.

## Introduction

### About this project

The {{ HPC }} is a general-purpose template for Python libraries and applications,
released under the [MIT license]
and hosted on [GitHub][hypermodern python cookiecutter].

The main objective of this project template is to
enable current best practices
through modern Python tooling.
Our goals are to:

- focus on simplicity and minimalism,
- promote code quality through automation, and
- provide reliable and repeatable processes,

all the way from local testing to publishing releases.

Projects are created from the template using [Cookiecutter],
a project scaffolding tool built on top of the [Jinja] template engine.

The project template is centered around the following tools:

- [Poetry] for packaging and dependency management
- [Nox] for automation of checks and other development tasks
- [GitHub Actions] for continuous integration and delivery

(features)=

### Features

Here is a detailed list of features for this Python template:

```{eval-rst}
.. include:: ../README.md
   :parser: myst_parser.sphinx_
   :start-after: <!-- features-begin -->
   :end-before: <!-- features-end -->

```

### Version policy

The {{ HPC }} uses [Calendar Versioning] with a `YYYY.MM.DD` versioning scheme.

The current stable release is [2021.11.26].

(installation)=

## Installation

### System requirements

You need a recent Windows, Linux, Unix, or Mac system with [git] installed.

:::{note}
When working with this template on Windows,
configure your text editor or IDE
to use only [UNIX-style line endings](https://en.wikipedia.org/wiki/Newline) (line feeds).

The project template contains a [.gitattributes] file
which enables end-of-line normalization for your entire working tree.
Additionally, the [Prettier] code formatter converts line endings to line feeds.
Windows-style line endings (`CRLF`) should therefore never make it into your Git repository.

Nonetheless, configuring your editor for line feeds is recommended
to avoid complaints from the [pre-commit] hook for Prettier.
:::

### Getting Python (Windows)

If you're on Windows,
download the recommended installer for the latest stable release of Python
from the official [Python website](https://www.python.org/).
Before clicking **Install now**,
enable the option to add Python to your `PATH` environment variable.

Verify your installation by checking the output of the following commands in a new terminal window:

```
python -VV
py -VV
```

Both of these commands should display the latest Python version, 3.10.

For local testing with multiple Python versions,
repeat these steps for the latest bugfix releases of Python 3.7+,
with the following changes:

- Do _not_ enable the option to add Python to the `PATH` environment variable.
- `py -VV` and `python -VV` should still display the version of the latest stable release.
- `py -X.Y -VV` (e.g. `py -3.7 -VV`) should display the exact version you just installed.

Note that binary installers are not provided for security releases.

### Getting Python (Mac, Linux, Unix)

If you're on a Mac, Linux, or Unix system,
use [pyenv] for installing and managing Python versions.
Please refer to the documentation of this project
for detailed installation and usage instructions.
(The following instructions assume that
your system already has [bash] and [curl] installed.)

Install [pyenv] like this:

```console
$ curl https://pyenv.run | bash
```

Add the following lines to your `~/.bashrc`:

```sh
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Install the Python build dependencies for your platform,
using one of the commands listed in the
[official instructions](https://github.com/pyenv/pyenv/wiki/Common-build-problems).

Install the latest point release of every supported Python version.
This project template supports Python 3.7, 3.8, 3.9, and 3.10.

```console
$ pyenv install 3.7.12
$ pyenv install 3.8.12
$ pyenv install 3.9.10
$ pyenv install 3.10.2
```

After creating your project (see {ref}`below <Creating a project>`),
you can make these Python versions accessible in the project directory,
using the following command:

```console
$ pyenv local 3.10.2 3.9.10 3.8.12 3.7.12
```

The first version listed is the one used when you type plain `python`.
Every version can be used by invoking `python<major.minor>`.
For example, use `python3.7` to invoke Python 3.7.

### Requirements

:::{note}
It is recommended to use [pipx] to install Python tools
which are not specific to a single project.
Please refer to the official documentation
for detailed installation and usage instructions.
If you decide to skip `pipx` installation,
use [pip install] with the `--user` option instead.
:::

You need four tools to use this template:

- [Cookiecutter] to create projects from the template,
- [Poetry] to manage packaging and dependencies
- [Nox] to automate checks and other tasks
- [nox-poetry] for using Poetry in Nox sessions

Install [Cookiecutter] using pipx:

```console
$ pipx install cookiecutter
```

Install [Poetry] by downloading and running [install-poetry.py]:

```console
$ python install-poetry.py
```

Install [Nox] and [nox-poetry] using pipx:

```console
$ pipx install nox
$ pipx inject nox nox-poetry
```

Remember to upgrade these tools regularly:

```console
$ pipx upgrade cookiecutter
$ pipx upgrade --include-injected nox
$ poetry self update
```

## Project creation

(creating-a-project)=

### Creating a project

Create a project from this template
by pointing Cookiecutter to its [GitHub repository][hypermodern python cookiecutter].
Use the `--checkout` option with the [current stable release][2021.11.26]:

```console
$ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python \
  --checkout="2021.11.26"
```

Cookiecutter downloads the template,
and asks you a series of questions about project variables,
for example, how you wish your project to be named.
When you have answered these questions,
your project is generated in the current directory,
using a subdirectory with the same name as your project.

Here is a complete list of the project variables defined by this template:

```{eval-rst}
.. table:: Project variables
   :widths: auto

   ====================== ================================= ===================================
   Variable               Description                       Example
   ====================== ================================= ===================================
   ``project_name``       Project name on PyPI and GitHub   ``hypermodern-python``
   ``package_name``       Import name of the package        ``hypermodern_python``
   ``friendly_name``      Friendly project name             ``Hypermodern Python``
   ``author``             Primary author                    Katherine Johnson
   ``email``              E-mail address of the author      katherine@example.com
   ``github_user``        GitHub username of the author     ``katherine``
   ``version``            Initial project version           ``0.0.0``
   ``copyright_year``     The project copyright year        ``2022``
   ``license``            The project license               ``MIT``
   ``development_status`` Development status of the project ``Development Status :: 3 - Alpha``
   ====================== ================================= ===================================
```

:::{note}
The initial project version should be the latest release on [PyPI],
or `0.0.0` for an unreleased package.
See [The Release workflow] for details.
:::

Your choices are recorded in the file `.cookiecutter.json` in the generated project,
together with the URL of this Cookiecutter template.
Having this [JSON] file in the project makes it possible later on
to update your project with changes from the Cookiecutter template,
using tools such as [cupper].

In the remainder of this guide,
`<project>` and `<package>` are used
to refer to the project and package names, respectively.
By default, their only difference is that
the project name uses hyphens (_kebab case_),
whereas the package name uses underscores (_snake case_).

### Uploading to GitHub

This project template is designed for use with [GitHub].
After generating the project,
your next steps are to create a Git repository and upload it to GitHub.

Change to the root directory of your new project,
initialize a Git repository, and
create a commit for the initial project structure.
In the commands below,
replace `<project>` by the name of your project.

```console
$ cd <project>
$ git init
$ git add .
$ git commit
```

Use the following command to ensure your default branch is called `main`,
which is the [default branch name for GitHub repositories](https://github.com/github/renaming).

```console
$ git branch --move --force main
```

Create an empty repository on [GitHub],
using the project name you chose when you generated the project.

:::{note}
Do not include a `README.md`, `LICENSE`, or `.gitignore`.
These files are provided by the project template.
:::

Finally, upload your repository to GitHub.
In the commands below, replace `<username>` by your GitHub username,
and `<project>` by the name of your project.

```console
$ git remote add origin git@github.com:<username>/<project>.git
$ git push --set-upstream origin main
```

Now may be a good time to set up Continuous Integration for your repository.
Refer to the section {ref}`External services`
for detailed instructions.

## Project overview

### Files and directories

This section provides an overview of all the files generated for your project.

Let's start with the directory layout:

```{eval-rst}
.. table:: Directories
   :widths: auto

   ===================================== ===============================
   ``src/<package>``                     Python package
   ``tests``                             Test suite
   ``docs``                              Documentation
   ``.github/workflows``                 GitHub Actions workflows
   ===================================== ===============================
```

The Python package is located in the `src/<package>` directory.
For more details on these files, refer to the section {ref}`The initial package`.

```{eval-rst}
.. table:: Python package
   :widths: auto

   ===================================== ===============================
   ``src/<project>/py.typed``            Marker file for `PEP 561`_
   ``src/<project>/__init__.py``         Package initialization
   ``src/<project>/__main__.py``         Command-line interface
   ===================================== ===============================
```

The test suite is located in the `tests` directory.
For more details on these files, refer to the section {ref}`The test suite`.

```{eval-rst}
.. table:: Test suite
   :widths: auto

   ===================================== ===============================
   ``tests/__init__.py``                 Test package initialization
   ``tests/test_main.py``                Test cases for ``__main__``
   ===================================== ===============================
```

The project documentation is written in [Markdown].
The documentation files in the top-level directory are rendered on [GitHub]:

```{eval-rst}
.. table:: Documentation files (top-level)
   :widths: auto

   ====================== ============================================
   ``README.md``          Project description for GitHub and PyPI
   ``CONTRIBUTING.md``    Contributor Guide
   ``CODE_OF_CONDUCT.md`` Code of Conduct
   ``LICENSE``            License
   ====================== ============================================
```

The files in the `docs` directory are
built using {ref}`Sphinx <Documentation>` and [MyST].
The Sphinx documentation is hosted on {ref}`Read the Docs <Read the Docs integration>`:

```{eval-rst}
.. table:: Documentation files (Sphinx)
   :widths: auto

   ===================== =======================================================
   ``index.md``          Main document
   ``contributing.md``   Contributor Guide (via include)
   ``codeofconduct.md``  Code of Conduct (via include)
   ``license.md``        License (via include)
   ``reference.md``      API reference
   ``usage.md``          Command-line reference
   ===================== =======================================================
```

The `.github/workflows` directory contains the {ref}`GitHub Actions workflows <GitHub Actions workflows>`:

```{eval-rst}
.. table:: GitHub Actions workflows
   :widths: auto

   ======================= ===============================
   ``release.yml``         :ref:`The Release workflow`
   ``tests.yml``           :ref:`The Tests workflow`
   ``labeler.yml``         :ref:`The Labeler workflow`
   ======================= ===============================
```

The project contains many configuration files for developer tools.
Most of these are located in the top-level directory.
The table below lists these files,
and links each file to a section with more details.

```{eval-rst}
.. table:: Configuration files
   :widths: auto

   ===================================== ========================================
   ``.cookiecutter.json``                :ref:`Project variables <Creating a project>`
   ``.darglint``                         Configuration for :ref:`darglint <darglint integration>`
   ``.github/dependabot.yml``            Configuration for :ref:`Dependabot <Dependabot integration>`
   ``.flake8``                           Configuration for :ref:`Flake8 <The Flake8 hook>`
   ``.gitattributes``                    `Git attributes <.gitattributes_>`__
   ``.gitignore``                        `Git ignore file <.gitignore_>`__
   ``.github/release-drafter.yml``       Configuration for :ref:`Release Drafter <The Release workflow>`
   ``.github/labels.yml``                Configuration for :ref:`GitHub Labeler <The Labeler workflow>`
   ``.pre-commit-config.yaml``           Configuration for :ref:`pre-commit <Linting with pre-commit>`
   ``.readthedocs.yml``                  Configuration for :ref:`Read the Docs <Read the Docs integration>`
   ``codecov.yml``                       Configuration for :ref:`Codecov <Codecov integration>`
   ``docs/conf.py``                      Configuration for :ref:`Sphinx <Documentation>`
   ``noxfile.py``                        Configuration for :ref:`Nox <Using Nox>`
   ``pyproject.toml``                    Configuration for :ref:`Poetry <Using Poetry>`,
                                         :ref:`Coverage.py <The coverage session>`,
                                         :ref:`isort <The isort hook>`,
                                         and :ref:`mypy <Type-checking with mypy>`
   ===================================== ========================================
```

The `pyproject.toml` file is described in more detail {ref}`below <The pyproject.toml file>`.

{ref}`Dependencies <Managing dependencies>` are managed by [Poetry]
and declared in the {ref}`pyproject.toml <The pyproject.toml file>` file.
The table below lists some additional files with pinned dependencies.
Follow the links for more details on these.

```{eval-rst}
.. table:: Dependency files
   :widths: auto

   ===================================== ================================
   ``poetry.lock``                       :ref:`Poetry lock file <The lock file>`
   ``docs/requirements.txt``             Requirements file for :ref:`Read the Docs <Read the Docs integration>`
   ``.github/workflows/constraints.txt`` Constraints file for :ref:`GitHub Actions workflows <Workflow constraints>`
   ===================================== ================================

```

(the-initial-package)=

### The initial package

You can find the initial Python package in your generated project
under the `src` directory:

```
src
└── <package>
    ├── __init__.py
    ├── __main__.py
    └── py.typed
```

`__init__.py`

: This file declares the directory as a [Python package],
  and contains any package initialization code.

`__main__.py`

: The [__main__](https://docs.python.org/3/library/__main__.html) module defines the entry point for the command-line interface.
  The command-line interface is implemented using the [Click] library,
  and supports `--help` and `--version` options.
  When the package is installed,
  a script named `<project>` is placed
  in the Python installation or virtual environment.
  This allows you to invoke the command-line interface using only the project name:

  ```console
  $ poetry run <project>  # during development
  $ <project>             # after installation
  ```

  The command-line interface can also be invoked
  by specifying a Python interpreter and the package name:

  ```console
  $ python -m <package> [<options>]
  ```

`py.typed`

: This is an empty marker file,
  which declares that your package supports typing
  and is distributed with its own type information
  ([PEP 561][pep 561]).
  This allows people using your package
  to type-check their Python code against it.

(the-test-suite)=

### The test suite

Tests are written using the [pytest] testing framework,
the _de facto_ standard for testing in Python.

The test suite is located in the `tests` directory:

```
tests
├── __init__.py
└── test_main.py
```

The test suite is [declared as a package](https://docs.pytest.org/en/latest/explanation/goodpractices.html#choosing-a-test-layout-import-rules),
and mirrors the source layout of the package under test.
The file `test_main.py` contains tests for the `__main__` module.

Initially, the test suite contains a single test case,
checking whether the program exits with a status code of zero.
It also provides a [test fixture] using [click.testing.CliRunner],
a helper class for invoking the program from within tests.

For details on how to run the test suite,
refer to the section {ref}`The tests session`.

(documentation)=

### Documentation

The project documentation is written in [Markdown]
and processed by the [Sphinx] documentation engine using the [MyST] extension.

The top-level directory contains several stand-alone documentation files:

`README.md`

: This file is your main project page and displayed on GitHub and PyPI.

`CONTRIBUTING.md`

: The Contributor Guide explains how other people can contribute to your project.

`CODE_OF_CONDUCT.md`

: The Code of Conduct outlines the behavior
  expected from participants of your project.
  It is adapted from the [Contributor Covenant], version 2.1.

`LICENSE.md`

: This file contains the text of your project's license.

:::{note}
The files above are also rendered on GitHub and PyPI.
Keep them in plain Markdown, without [MyST] syntax extensions.
:::

The documentation files in the `docs` directory are built using [Sphinx] and [MyST]:

`index.md`

: This is the main documentation page.
  It includes the project description from `README.md`.
  This file also defines the navigation menu,
  with links to other documentation pages.
  The *Changelog* menu entry
  links to the [GitHub Releases][github release] page of your project.

`contributing.md`

: This file includes the Contributor Guide from `CONTRIBUTING.md`.

`codeofconduct.md`

: This file includes the Code of Conduct from `CODE_OF_CONDUCT.md`.

`license.md`

: This file includes the license from `LICENSE.md`.

`reference.md`

: The API reference for your project.
  It is generated from docstrings and type annotations in the source code,
  using the [autodoc] and [napoleon] extensions.

`usage.md`

: The command-line reference for your project.
  It is generated by inspecting the [click] entry-point in your package,
  using the [sphinx-click] extension.

The `docs` directory contains two more files:

`conf.py`

: This Python file contains the [Sphinx configuration](https://www.sphinx-doc.org/en/master/usage/configuration.html).

`requirements.txt`

: The requirements file pins the build dependencies for the Sphinx documentation.
  This file is only used on Read the Docs.

The project documentation is built and hosted on
{ref}`Read the Docs <Read the Docs integration>`,
and uses the [furo] Sphinx theme.

You can also build the documentation locally using Nox,
see {ref}`The docs session`.

## Packaging

(the-pyproject-toml-file)=

### The pyproject.toml file

The configuration file for the Python package is located
in the root directory of the project,
and named `pyproject.toml`.
It uses the [TOML] configuration file format,
and contains two sections---_tables_ in TOML parlance---,
specified in [PEP 517][pep 517] and [518][pep 518]:

- The `build-system` table
  declares the requirements and the entry point
  used to build a distribution package for the project.
  This template uses [Poetry] as the build system.
- The `tool` table contains sub-tables
  where tools can store configuration under their [PyPI] name.

```{eval-rst}
.. table:: Tool configurations in pyproject.toml
   :widths: auto

   ======================= ===============================
   ``tool.coverage``       Configuration for Coverage.py_
   ``tool.isort``          Configuration for isort_
   ``tool.mypy``           Configuration for mypy_
   ``tool.poetry``         Configuration for Poetry_
   ======================= ===============================
```

The `tool.poetry` table
contains the metadata for your package,
such as its name, version, and authors,
as well as the list of dependencies for the package.
Please refer to the [Poetry documentation][pyproject.toml]
for a detailed description of each configuration key.

(version-constraints)=

### Version constraints

:::{admonition} TL;DR
This project template omits upper bounds from all version constraints.

You are encouraged to manually remove upper bounds
for dependencies you add to your project using Poetry:

1. Replace `^1.2.3` with `>=1.2.3` in `pyproject.toml`
2. Run `poetry lock --no-update` to update `poetry.lock`
:::

[Version constraints][versions and constraints] express
which versions of dependencies are compatible with your project.
In the case of core dependencies,
they are also a part of distribution packages,
and as such affect end-users of your package.

:::{note}
Dependencies are Python packages used by your project,
and they come in two types:

- _Core dependencies_ are required by users running your code,
  and typically consist of third-party libraries imported by your package.
  When your package is distributed,
  the [package metadata] includes these dependencies,
  allowing tools like [pip] to automatically install them alongside your package.
- _Development dependencies_ are only required by developers working on your code.
  Examples are applications used to run tests,
  check code for style and correctness,
  or to build documentation.
  These dependencies are not a part of distribution packages,
  because users do not require them to run your code.
:::

For every dependency added to your project,
Poetry writes a version constraint to `pyproject.toml`.
Dependencies are kept in two TOML tables:

- `tool.poetry.dependencies`---for core dependencies
- `tool.poetry.dev-dependencies`---for development dependencies

By default, version constraints added by Poetry have both a lower and an upper bound:

- The lower bound requires users of your package to have at least the version
  that was current when you added the dependency.
- The upper bound allows users to upgrade to newer releases of dependencies,
  as long as the version number does not indicate a breaking change.

According to the [Semantic Versioning] standard,
only major releases may contain breaking changes,
once a project has reached version 1.0.0.
A major release is one that increments the major version
(the first component of the version identifier).
An example for such a version constraint would be `^1.2.3`,
which is a Poetry-specific shorthand equivalent to `>= 1.2.3, < 2`.

This project template omits upper bounds from all version constraints,
in a conscious departure from Poetry's defaults.
There are two separate reasons for removing version caps,
one principled, the other pragmatic:

1. Version caps lead to problems in the Python ecosystem due to its flat dependency management.
2. Version caps lead to frequent merge conflicts between dependency updates.

The first point is treated in detail in the following articles:

- [Should You Use Upper Bound Version Constraints?](https://iscinumpy.dev/post/bound-version-constraints/) and [Poetry Versions](https://iscinumpy.dev/post/poetry-versions/) by Henry Schreiner
- [Semantic Versioning Will Not Save You](https://hynek.me/articles/semver-will-not-save-you/) by Hynek Schlawack
- [Version numbers: how to use them?](https://bernat.tech/posts/version-numbers/) by Bernát Gábor
- [Why I don't like SemVer anymore](https://snarky.ca/why-i-dont-like-semver/) by Brett Cannon

The second point is ultimately due to the fact that
every updated version constraint changes a hashsum in the `poetry.lock` file.
This means that PRs updating version constraints will _always_ conflict with each other.

:::{note}
The problem with merge conflicts is greatly exacerbated by a [Dependabot issue][dependabot issue 4435]:
Dependabot updates version constraints in `pyproject.toml`
even when the version constraint already covered the new version.
This can be avoided using a configuration setting
where only the lock file is ever updated, not the version constraints.
Omitting version caps makes the lockfile-only strategy a viable alternative.
:::

Poetry will still add `^1.2.3`-style version constraints whenever you add a dependency.
You should edit the version constraint in `pyproject.toml`,
replacing `^1.2.3` with `>=1.2.3` to remove the upper bound.
Then update the lock file by invoking `poetry lock --no-update`.

(the-lock-file)=

### The lock file

Poetry records the exact version of each direct and indirect dependency
in its lock file, named `poetry.lock` and located in the root directory of the project.
The lock file does not affect users of the package,
because its contents are not included in distribution packages.

The lock file is useful for a number of reasons:

- It ensures that local checks run in the same environment as on the CI server,
  making the CI predictable and deterministic.
- When collaborating with other developers,
  it allows everybody to use the same development environment.
- When deploying an application, the lock file helps you
  keep production and development environments as similar as possible
  ([dev-prod parity]).

For these reasons, the lock file should be kept under source control.

### Dependencies

This project template has a core dependency on [Click],
a library for creating command-line interfaces.
The template also comes with various development dependencies.
See the table below for an overview of the dependencies of generated projects:

```{eval-rst}
.. table:: Dependencies
   :widths: auto

   ====================== ====================================================================================
   black_                 The uncompromising code formatter.
   click_                 Composable command line interface toolkit
   coverage__             Code coverage measurement for Python
   darglint_              A utility for ensuring Google-style docstrings stay up to date with the source code.
   flake8_                the modular source code checker: pep8 pyflakes and co
   flake8-bandit_         Automated security testing with bandit and flake8.
   flake8-bugbear_        A plugin for flake8 finding likely bugs and design problems in your program.
   flake8-docstrings_     Extension for flake8 which uses pydocstyle to check docstrings
   flake8-rst-docstrings_ Python docstring reStructuredText (RST) validator
   furo_                  A clean customisable Sphinx documentation theme.
   isort_                 A Python utility / library to sort Python imports.
   mypy_                  Optional static typing for Python
   pep8-naming_           Check PEP-8 naming conventions, plugin for flake8
   pre-commit_            A framework for managing and maintaining multi-language pre-commit hooks.
   pre-commit-hooks_      Some out-of-the-box hooks for pre-commit.
   pygments_              Pygments is a syntax highlighting package written in Python.
   pytest_                pytest: simple powerful testing with Python
   pyupgrade_             A tool to automatically upgrade syntax for newer versions.
   safety_                Checks installed dependencies for known vulnerabilities.
   sphinx_                Python documentation generator
   sphinx-autobuild_      Rebuild Sphinx documentation on changes, with live-reload in the browser.
   sphinx-click_          Sphinx extension that automatically documents click applications
   typeguard_             Run-time type checker for Python
   xdoctest_              A rewrite of the builtin doctest module
   ====================== ====================================================================================

__ Coverage.py_
```

(using-poetry)=

## Using Poetry

[Poetry] manages packaging and dependencies for Python projects.

(managing-dependencies)=

### Managing dependencies

Use the command [poetry show] to
see the full list of direct and indirect dependencies of your package:

```console
$ poetry show
```

Use the command [poetry add] to add a dependency for your package:

```console
$ poetry add foobar        # for core dependencies
$ poetry add --dev foobar  # for development dependencies
```

:::{important}
It is recommended to remove the upper bound from the version constraint added by Poetry:

1. Edit `pyproject.toml` to replace `^1.2.3` with `>=1.2.3` in the dependency entry
2. Update `poetry.lock` using the command `poetry lock --no-update`

See [Version constraints] for more details.
:::

Use the command [poetry remove] to remove a dependency from your package:

```console
$ poetry remove foobar
```

Use the command [poetry update] to upgrade the dependency to a new release:

```console
$ poetry update foobar
```

:::{note}
Dependencies in the {{ HPC }} are managed by {ref}`Dependabot <Dependabot integration>`.
When newer versions of dependencies become available,
Dependabot updates the `poetry.lock` file and submits a pull request.
:::

### Installing the package for development

Poetry manages a virtual environment for your project,
which contains your package, its core dependencies, and the development dependencies.
All dependencies are kept at the versions specified by the lock file.

:::{note}
A [virtual environment] gives your project
an isolated runtime environment,
consisting of a specific Python version and
an independent set of installed Python packages.
This way, the dependencies of your current project
do not interfere with the system-wide Python installation,
or other projects you're working on.
:::

You can install your package and its dependencies
into Poetry's virtual environment
using the command [poetry install].

```console
$ poetry install
```

This command performs a so-called [editable install](https://pip.pypa.io/en/stable/cli/pip_install/#install-editable) of your package:
Instead of building and installing a distribution package,
it creates a special `.egg-link` file that links to your local source code.
This means that code edits are directly visible in the environment
without the need to reinstall your package.

Installing your package implicitly creates the virtual environment
if it does not exist yet,
using the currently active Python interpreter,
or the first one found
which satisfies the Python versions supported by your project.

### Managing environments

You can create environments explicitly
with the [poetry env] command,
specifying the desired Python version.
This allows you to create an environment
for every Python version supported by your project,
and easily switch between them:

```console
$ poetry env use 3.7
$ poetry env use 3.8
$ poetry env use 3.9
$ poetry env use 3.10
```

Only one Poetry environment can be active at any time.
Note that `3.10` comes last,
to ensure that the current Python release is the active environment.
Install your package with `poetry install` into each environment after creating it.

Use the command `poetry env list` to list the available environments:

```console
$ poetry env list
```

Use the command `poetry env remove` to remove an environment:

```console
$ poetry env remove <version>
```

Use the command `poetry env info` to show information about the active environment:

```console
$ poetry env info
```

### Running commands

You can run an interactive Python session inside the active environment
using the command [poetry run]:

```console
$ poetry run python
```

The same command allows you to invoke the command-line interface of your project:

```console
$ poetry run <project>
```

You can also run developer tools, such as [pytest]:

```console
$ poetry run pytest
```

While it is handy to have developer tools available in the Poetry environment,
it is usually recommended to run these using Nox,
as described in the section {ref}`Using Nox`.

### Building and distributing the package

:::{note}
With the {{ HPC }},
building and distributing your package
is taken care of by [GitHub Actions].
For more information,
see the section {ref}`The Release workflow`.
:::

This section gives a short overview of
how you can build and distribute your package
from the command line,
using the following Poetry commands:

```console
$ poetry build
$ poetry publish
```

Building the package is done with the [python build] command,
which generates _distribution packages_
in the `dist` directory of your project.
These are compressed archives that
an end-user can download and install on their system.
They come in two flavours:
source (or _sdist_) archives, and
binary packages in the [wheel] format.

Publishing the package is done with the [python publish] command,
which uploads the distribution packages
to your account on [PyPI],
the official Python package registry.

### Installing the package

Once your package is on PyPI,
others can install it with [pip], [pipx], or Poetry:

```console
$ pip install <project>
$ pipx install <project>
$ poetry add <project>
```

While [pip] is the workhorse of the Python packaging ecosystem,
you should use higher-level tools to install your package:

- If the package is an application, install it with [pipx].
- If the package is a library, install it with [poetry add] in other projects.

The primary benefit of these installation methods is that
your package is installed into an isolated environment,
without polluting the system environment,
or the environments of other applications.
This way,
applications can use specific versions of their direct and indirect dependencies,
without getting in each other's way.

If the other project is not managed by Poetry,
use whatever package manager the other project uses.
You can always install your project into a virtual environment with plain [pip].

(using-nox)=

## Using Nox

[Nox] automates testing in multiple Python environments.
Like its older sibling [tox],
Nox makes it easy to run any kind of job in an isolated environment,
with only those dependencies installed that the job needs.

Nox sessions are defined in a Python file
named `noxfile.py` and located in the project directory.
They consist of a virtual environment
and a set of commands to run in that environment.

While Poetry environments allow you to
interact with your package during development,
Nox environments are used to run developer tools
in a reliable and repeatable way across Python versions.

Most sessions are run with every supported Python version.
Other sessions are only run with the current stable Python version,
for example the session used to build the documentation.

### Running sessions

If you invoke Nox by itself, it will run the full test suite:

```console
$ nox
```

This includes tests, linters, type checks, and more.
For the full list, please refer to the table [below][table of nox sessions].

The list of sessions run by default can be configured
by editing `nox.options.sessions` in `noxfile.py`.
Currently the list only excludes the [docs session][the docs session]
(which spawns an HTTP server)
and the [coverage session][the coverage session]
(which is triggered by the [tests session][the tests session]).

You can also run a specific Nox session, using the `--session` option.
For example, build the documentation like this:

```console
$ nox --session=docs
```

Print a list of the available Nox sessions
using the `--list-sessions` option:

```console
$ nox --list-sessions
```

Nox creates virtual environments from scratch on each invocation.
You can speed things up by passing the
[--reuse-existing-virtualenvs] option,
or the equivalent short option `-r`.
For example, the following may be more practical during development
(this will only run tests and type checks, on the current Python release):

```console
$ nox -p 3.10 -rs tests mypy
```

Many sessions accept additional options after `--` separator.
For example, the following command runs a specific test module:

```console
$ nox --session=tests -- tests/test_main.py
```

### Overview of Nox sessions

(table-of-nox-sessions)=

The following table gives an overview of the available Nox sessions:

```{eval-rst}
.. table:: Nox sessions
   :widths: auto

   ========================================== ===================================== ================== =========
   Session                                    Description                           Python              Default
   ========================================== ===================================== ================== =========
   :ref:`coverage <The coverage session>`     Report coverage with Coverage.py_     ``3.10``              (✓)
   :ref:`docs <The docs session>`             Build and serve Sphinx_ documentation ``3.10``
   :ref:`docs-build <The docs-build session>` Build Sphinx_ documentation           ``3.10``               ✓
   :ref:`mypy <The mypy session>`             Type-check with mypy_                 ``3.7`` … ``3.10``     ✓
   :ref:`pre-commit <The pre-commit session>` Lint with pre-commit_                 ``3.10``               ✓
   :ref:`safety <The safety session>`         Scan dependencies with Safety_        ``3.10``               ✓
   :ref:`tests <The tests session>`           Run tests with pytest_                ``3.7`` … ``3.10``     ✓
   :ref:`typeguard <The typeguard session>`   Type-check with Typeguard_            ``3.10``               ✓
   :ref:`xdoctest <The xdoctest session>`     Run examples with xdoctest_           ``3.7`` … ``3.10``     ✓
   ========================================== ===================================== ================== =========

```

(the-docs-session)=

### The docs session

Build the documentation using the Nox session `docs`:

```console
$ nox --session=docs
```

The docs session runs the command `sphinx-autobuild` to generate the HTML documentation from the Sphinx directory.
This tool has several advantages over `sphinx-build` when you are editing the documentation files:

- It rebuilds the documentation whenever a change is detected.
- It spins up a web server with live reloading.
- It opens the location of the web server in your browser.

Use the `--` separator to pass additional options.
For example, to treat warnings as errors and run in nit-picky mode:

```console
$ nox --session=docs -- -W -n docs docs/_build
```

This Nox session always runs with the current major release of Python.

(the-docs-build-session)=

### The docs-build session

The `docs-build` session runs the command `sphinx-build` to generate the HTML documentation from the Sphinx directory.

This session is meant to be run as a part of automated checks.
Use the interactive `docs` session instead while you're editing the documentation.

This Nox session always runs with the current major release of Python.

(the-mypy-session)=

### The mypy session

[mypy] is the pioneer and _de facto_ reference implementation of static type checking in Python.
Learn more about it in the section {ref}`Type-checking with mypy`.

Run mypy using Nox:

```console
$ nox --session=mypy
```

You can also run the type checker with a specific Python version.
For example, the following command runs mypy
using the current stable release of Python:

```console
$ nox --session=mypy --python=3.10
```

Use the separator `--` to pass additional options and arguments to `mypy`.
For example, the following command type-checks only the `__main__` module:

```console
$ nox --session=mypy -- src/<package>/__main__.py
```

(the-pre-commit-session)=

### The pre-commit session

[pre-commit] is a multi-language linter framework and a Git hook manager.
Learn more about it in the section {ref}`Linting with pre-commit`.

Run pre-commit from Nox using the `pre-commit` session:

```console
$ nox --session=pre-commit
```

This session always runs with the current stable release of Python.

Use the separator `--` to pass additional options to `pre-commit`.
For example, the following command installs the pre-commit hooks,
so they run automatically on every commit you make:

```console
$ nox --session=pre-commit -- install
```

(the-safety-session)=

### The safety session

[Safety] checks the dependencies of your project for known security vulnerabilities,
using a curated database of insecure Python packages.
The {{ HPC }} uses the [poetry export] command
to convert Poetry's lock file to a [requirements file],
for consumption by Safety.

Run [Safety] using the `safety` session:

```console
$ nox --session=safety
```

This session always runs with the current stable release of Python.

(the-tests-session)=

### The tests session

Tests are written using the [pytest] testing framework.
Learn more about it in the section {ref}`The test suite`.

Run the test suite using the Nox session `tests`:

```console
$ nox --session=tests
```

The tests session runs the test suite against the installed code.
More specifically, the session builds a wheel from your project and
installs it into the Nox environment,
with dependencies pinned as specified by Poetry's lock file.

You can also run the test suite with a specific Python version.
For example, the following command runs the test suite
using the current stable release of Python:

```console
$ nox --session=tests --python=3.10
```

Use the separator `--` to pass additional options to `pytest`.
For example, the following command runs only the test case `test_main_succeeds`:

```console
$ nox --session=tests -- -k test_main_succeeds
```

The tests session also installs [pygments], a Python syntax highlighter.
It is used by pytest to highlight code in tracebacks,
improving the readability of test failures.

(the-coverage-session)=

### The coverage session

:::{note}
_Test coverage_ is a measure of the degree to which
the source code of your program is executed
while running its test suite.
:::

The coverage session prints a detailed coverage report to the terminal,
combining the coverage data collected
during the {ref}`tests session <The tests session>`.
If the total coverage is below 100%,
the coverage session fails.
Code coverage is measured using [Coverage.py].

The coverage session is triggered by the tests session,
and runs after all other sessions have completed.
This allows it to combine the coverage data for different Python versions.

You can also run the session manually:

```console
$ nox --session=coverage
```

Use the `--` separator to pass arguments to the `coverage` command.
For example, here's how you would generate an HTML report
in the `htmlcov` directory:

```console
$ nox -rs coverage -- html
```

[Coverage.py] is configured in the `pyproject.toml` file,
using the `tool.coverage` table.
The configuration informs the tool about your package name and source tree layout.
It also enables branch analysis and the display of line numbers for missing coverage,
and specifies the target coverage percentage.
Coverage is measured for the package as well as [the test suite itself](https://nedbatchelder.com/blog/202008/you_should_include_your_tests_in_coverage.html).

During continuous integration,
coverage data is uploaded to the [Codecov] reporting service.
For details, see the sections about
{ref}`Codecov <Codecov integration>` and
{ref}`The Tests workflow`.

(the-typeguard-session)=

### The typeguard session

[Typeguard] is a runtime type checker and [pytest] plugin.
It can type-check function calls during test runs via an [import hook](https://docs.python.org/3/reference/import.html#import-hooks).

Typeguard checks that arguments passed to functions
match the type annotations of the function parameters,
and that the return value provided by the function
matches the return type annotation.
In the case of generator functions,
Typeguard checks the yields, sends and the return value
against the `Generator` annotation.

Run [Typeguard] using Nox:

```console
$ nox --session=typeguard
```

The typeguard session runs the test suite with runtime type-checking enabled.
It is similar to the {ref}`tests session <The tests session>`,
with the difference that your package is instrumented by Typeguard.

This session always runs with the current stable release of Python.

Use the separator `--` to pass additional options and arguments to pytest.
For example, the following command runs only tests for the `__main__` module:

```console
$ nox --session=typeguard -- tests/test_main.py
```

:::{note}
Typeguard generates a warning about missing type annotations for a Click object.
This is due to the fact that `__main__.main` is wrapped by a decorator,
and its type annotations only apply to the inner function,
not the resulting object as seen by the test suite.
:::

(the-xdoctest-session)=

### The xdoctest session

The [xdoctest] tool
runs examples in your docstrings and
compares the actual output to the expected output as per the docstring.
This serves multiple purposes:

- The example is checked for correctness.
- You ensure that the documentation is up-to-date.
- Your codebase gets additional test coverage for free.

Run the tool using the Nox session `xdoctest`:

```console
$ nox --session=xdoctest
```

You can also run the test suite with a specific Python version.
For example, the following command runs the examples
using the current stable release of Python:

```console
$ nox --session=xdoctest --python=3.10
```

By default, the Nox session uses the `all` subcommand to run all examples.
You can also list examples using the `list` subcommand,
or run specific examples:

```console
$ nox --session=xdoctest -- list
```

(linting-with-pre-commit)=

## Linting with pre-commit

[pre-commit] is a multi-language linter framework and a Git hook manager.
It allows you to
integrate linters and formatters into your Git workflow,
even when written in a language other than Python.

pre-commit is configured using the file `.pre-commit-config.yaml`
in the project directory.
Please refer to the [official documentation](https://pre-commit.com/#adding-pre-commit-plugins-to-your-project)
for details about the configuration file.

### Running pre-commit from Nox

pre-commit runs in a Nox session every time you invoke `nox`:

```console
$ nox
```

Run the pre-commit session explicitly like this:

```console
$ nox --session=pre-commit
```

The session is described in more detail in the section {ref}`The pre-commit session`.

### Running pre-commit from git

When installed as a [Git hook],
pre-commit runs automatically every time you invoke `git commit`.
The commit is aborted if any check fails.
When invoked in this mode, pre-commit only runs on files staged for the commit.

Install pre-commit as a Git hook by running the following command:

```console
$ nox --session=pre-commit -- install
```

### Managing hooks with pre-commit

Hooks in languages other than Python, such as `prettier`,
run in isolated environments managed by pre-commit.
To upgrade these hooks, use the [autoupdate](https://pre-commit.com/#pre-commit-autoupdate) command:

```console
$ nox --session=pre-commit -- autoupdate
```

### Python-language hooks

:::{note}
This section provides some background information about
how this project template integrates pre-commit with Poetry and Nox.
You can safely skip this section.
:::

Python-language hooks in the {{ HPC }} are not managed by pre-commit.
Instead, they are tracked as development dependencies in Poetry,
and installed into the Nox session alongside pre-commit itself.
As development dependencies, they are also present in the Poetry environment.

This approach has some advantages:

- All project dependencies are managed by Poetry.
- Hooks receive automatic upgrades from Dependabot.
- Nox can serve as a single entry point for all checks.
- Additional hook dependencies can be upgraded by a dependency manager.
  An example for this are Flake8 extensions.
  By contrast, `pre-commit autoupdate` does not include additional dependencies.
- Dependencies of dependencies (_subdependencies_) can be locked automatically,
  making checks more repeatable and deterministic.
- Linters and formatters are available in the Poetry environment,
  which is useful for editor integration.

There are also some drawbacks to this technique:

- This is not the officially supported way to integrate pre-commit hooks.
- The hook scripts installed by pre-commit do not activate the virtual environment
  in which pre-commit and the hooks are installed.
  To work around this limitation,
  the Nox session patches hook scripts on installation.
- Adding a hook is more work,
  including updating `pyproject.toml` and `noxfile.py`, and
  adding the hook definition to `pre-commit-config.yaml`.

You can always opt out of this integration method,
by removing the `repo: local` section from the configuration file,
and adding the official pre-commit hooks instead.
Don't forget to remove the hooks from Poetry's dependencies and from the Nox session.

:::{note}
Python-language hooks in the {{ HPC }} are defined as [system hooks](https://pre-commit.com/#system).
System hooks don't have their environments managed by pre-commit;
instead, pre-commit assumes that hook dependencies have already been installed
and are available in its environment.
The Nox session for pre-commit takes care of
installing the Python hooks alongside pre-commit.

Furthermore, the {{ HPC }} defines Python-language hooks as [repository-local hooks](https://pre-commit.com/#repository-local-hooks).
As such, hook definitions are not supplied by the hook repositories,
but by the project itself.
This makes it possible to override the hook language to `system`, as explained above.
:::

### Adding an official pre-commit hook

Adding the official pre-commit hook for a linter is straightforward.
Often you can simply copy a configuration snippet from the repository's `README`.
Otherwise, note the hook identifier from the `pre-commit-hooks.yaml` file,
and the git tag for the latest version.
Add the following section to your `pre-commit-config.yaml`, under `repos`:

```yaml
- repo: <hook repository>
  rev: <version tag>
  hooks:
    - id: <hook identifier>
```

While this technique also works for Python-language hooks,
it is recommended to integrate Python hooks with Nox and Poetry,
as shown in the next section.

### Adding a Python-language hook

Adding a Python-language hook to your project takes three steps:

- Add the hook as a Poetry development dependency.
- Install the hook in the Nox session for pre-commit.
- Add the hook to `pre-commit-config.yaml`.

For example, consider a linter named `awesome-linter`.

First, use Poetry to add the linter to your development dependencies:

```console
$ poetry add --dev awesome-linter
```

Next, update `noxfile.py` to add the linter to the pre-commit session:

```python
@nox.session(name="pre-commit", ...)
def precommit(session: Session) -> None:
    ...
    session.install(
        "awesome-linter",  # Install awesome-linter
        "black",
        "darglint",
        ...
    )
```

Finally, add the hook to `pre-commit-config.yaml` as follows:

- Locate the `pre-commit-hooks.yaml` file in the `awesome-linter` repository.
- Copy the entry for the hook (not just the hook identifier).
- Change `language:` from `python` to `system`.
- Add the hook definition to the `repo: local` section.

Depending on the linter, the hook definition might look somewhat like the following:

```yaml
repos:
  - repo: local
    hooks:
      # ...
      - id: awesome-linter
        name: Awesome Linter
        entry: awesome-linter
        language: system # was: python
        types: [python]
```

### Running checks on modified files

pre-commit runs checks on the _staged_ contents of files.
Any local modifications are stashed for the duration of the checks.
This is motivated by pre-commit's primary use case,
validating changes staged for a commit.

Requiring changes to be staged allows for a nice property:
Many pre-commit hooks support fixing offending lines automatically,
for example `black`, `prettier`, and `isort`.
When this happens,
your original changes are in the staging area,
while the fixes are in the work tree.
You can accept the fixes by staging them with `git add`
before committing again.

If you want to run linters or formatters on modified files,
and you do not want to stage the modifications just yet,
you can also invoke the tools via Poetry instead.
For example, use `poetry run flake8 <file>` to lint a modified file with Flake8.

### Overview of pre-commit hooks

The {{ HPC }} comes with a pre-commit configuration consisting of the following hooks:

```{eval-rst}
.. table:: pre-commit hooks
   :widths: auto

   ======================== ===============================================
   `black <Black_>`__       Run the Black_ code formatter
   `flake8 <Flake8_>`__     Run the Flake8_ linter
   isort_                   Rewrite source code to sort Python imports
   `prettier <Prettier_>`__ Run the Prettier_ code formatter
   pyupgrade_               Upgrade syntax to newer versions of Python
   check-added-large-files_ Prevent giant files from being committed
   check-toml_              Validate TOML_ files
   check-yaml_              Validate YAML_ files
   end-of-file-fixer_       Ensure files are terminated by a single newline
   trailing-whitespace_     Ensure lines do not contain trailing whitespace
   ======================== ===============================================
```

### The Black hook

[Black] is the uncompromising Python code formatter.
One of its greatest features is its lack of configurability.
Blackened code looks the same regardless of the project you're reading.

### The Prettier hook

[Prettier] is an opinionated code formatter for many languages,
including YAML, Markdown, and JavaScript.
Like Black, it has few options,
and the {{ HPC }} uses none of them.

(the-flake8-hook)=

### The Flake8 hook

[Flake8] is an extensible linter framework for Python.
For more details, see the section {ref}`Linting with Flake8`.

(the-isort-hook)=

### The isort hook

[isort] reorders imports in your Python code.
Imports are separated into three sections,
as recommended by [PEP 8][pep 8]: standard library, third party, first party.
There are two additional sections,
one at the top for [future imports](https://docs.python.org/3/library/__future__.html),
the other at the bottom for [relative imports](https://docs.python.org/3/reference/import.html#package-relative-imports).
Within each section, `from` imports follow normal imports.
Imports are then sorted alphabetically.

The {{ HPC }} activates the [Black profile](https://pycqa.github.io/isort/docs/configuration/black_compatibility.html) for compatibility with the Black code formatter.
Furthermore, the [force_single_line](https://pycqa.github.io/isort/docs/configuration/options.html#force-single-line) setting is enabled.
This splits imports onto separate lines to avoid merge conflicts.
Finally, two blank lines are enforced after imports for consistency,
via the [lines_after_imports](https://pycqa.github.io/isort/docs/configuration/options.html#lines-after-imports) setting.

### The pyupgrade hook

[pyupgrade] upgrades your source code
to newer versions of the Python language and standard library.
The tool analyzes the [abstract syntax tree](https://docs.python.org/3/library/ast.html) of the modules in your project,
replacing deprecated or legacy usages with modern idioms.

The minimum supported Python version is declared in the relevant section of `.pre-commit-config.yaml`.
You should change this setting whenever you drop support for an old version of Python.

### Hooks from pre-commit-hooks

The pre-commit configuration also includes several smaller hooks
from the [pre-commit-hooks] repository.

(linting-with-flake8)=

## Linting with Flake8

[Flake8] is an extensible linter framework for Python,
and a command-line utility to run the linters on your source code.
The {{ HPC }} integrates Flake8 via a [pre-commit] hook,
see the section {ref}`The Flake8 hook`.

The configuration file for Flake8 and its extensions
is named `.flake8` and located in the project directory.
For details about the configuration file, see the [official reference](https://flake8.pycqa.org/en/latest/user/configuration.html).

The sections below describe the linters in more detail.
Each section also notes any configuration settings applied by the {{ HPC }}.

### Overview of available plugins

Flake8 comes with a rich ecosystem of plugins.
The following table lists the Flake8 plugins used by the {{ HPC }},
and links to their lists of error codes.

```{eval-rst}
.. table:: Flake8 plugins
   :widths: auto

   ================================ ============================================= ======================================
   pyflakes_                        Find invalid Python code                      `F <pyflakes codes_>`__
   pycodestyle_                     Enforce style conventions from `PEP 8`_       `E,W <pycodestyle codes_>`__
   pep8-naming_                     Enforce naming conventions from `PEP 8`_      `N <pep8-naming codes_>`__
   pydocstyle_ / flake8-docstrings_ Enforce docstring conventions from `PEP 257`_ `D <pydocstyle codes_>`__
   flake8-rst-docstrings_           Find invalid reStructuredText_ in docstrings  `RST <flake8-rst-docstrings codes_>`__
   flake8-bugbear_                  Detect bugs and design problems               `B <flake8-bugbear codes_>`__
   mccabe_                          Limit the code complexity                     `C <mccabe codes_>`__
   darglint_                        Detect inaccurate docstrings                  `DAR <darglint codes_>`__
   Bandit_ / flake8-bandit_         Detect common security issues                 `S <Bandit codes_>`__
   ================================ ============================================= ======================================

```

### pyflakes

[pyflakes] parses Python source files and finds invalid code.
Warnings reported by this tool include
syntax errors,
undefined names,
unused imports or variables,
and more.
It is included with [Flake8] by default.

[Error codes][pyflakes codes] are prefixed by `F` for "flake".

### pycodestyle

[pycodestyle] checks your code against the style recommendations of [PEP 8][pep 8],
the official Python style guide.
The tool detects
whitespace and indentation issues,
deprecated features,
bare excepts,
and much more.
It is included with [Flake8] by default.

[Error codes][pycodestyle codes] are prefixed by `W` for warnings and `E` for errors.

The {{ HPC }} disables the following errors and warnings
for compatibility with [Black] and [flake8-bugbear]:

- `E203` (whitespace before `:`)
- `E501` (line too long)
- `W503` (line break before binary operator)

### pep8-naming

[pep8-naming] enforces the naming conventions from [PEP 8][pep 8].
Examples are the use of camel case for the names of classes,
the use of lowercase for the names of functions, arguments and variables,
or the convention to name the first argument of methods `self`.

[Error codes][pep8-naming codes] are prefixed by `N` for "naming".

### pydocstyle and flake8-docstrings

[pydocstyle] checks that docstrings comply with the recommendations of [PEP 257][pep 257]
and a configurable style convention.
It is integrated with Flake8 via the [flake8-docstrings] extension.
Warnings range from missing docstrings to
issues with whitespace, quoting, and docstring content.

[Error codes][pydocstyle codes] are prefixed by `D` for "docstring".

The {{ HPC }} selects the recommendations of the
[Google styleguide][google docstring style].
Here is an example of a function documented in Google style:

```python
def add(first: int, second: int) -> int:
    """Add two integers.

    Args:
        first: The first argument.
        second: The second argument.

    Returns:
        The sum of the arguments.
    """
```

### flake8-rst-docstrings

[flake8-rst-docstrings] validates docstring markup as [reStructuredText].
Docstrings must be valid reStructuredText
because they are used by Sphinx to generate the API reference.

[Error codes][flake8-rst-docstrings codes] are prefixed by `RST` for "reStructuredText",
and group issues into numerical blocks, by their severity and origin.

### flake8-bugbear

[flake8-bugbear] detects bugs and design problems.
The warnings are more opinionated than those of pyflakes or pycodestyle.
For example,
the plugin detects Python 2 constructs which have been removed in Python 3,
and likely bugs such as function arguments defaulting to empty lists or dictionaries.

[Error codes][flake8-bugbear-codes] are prefixed by `B` for "bugbear".

The {{ HPC }} also enables Bugbear's `B9` warnings,
which are disabled by default.
In particular, `B950` checks the maximum line length
like [pycodestyle]'s `E501`,
but with a tolerance margin of 10%.
This soft limit is set to 80 characters,
which is the value used by the Black code formatter.

### mccabe

[mccabe] checks the [code complexity][cyclomatic complexity]
of your Python package against a configured limit.
The tool is included with [Flake8].

[Error codes][mccabe codes] are prefixed by `C` for "complexity".

The {{ HPC }} limits code complexity to a value of 10.

(darglint-integration)=

### darglint

[darglint] checks that docstring descriptions match function definitions.
The tool has its own configuration file, named `.darglint`.

[Error codes][darglint codes] are prefixed by `DAR` for "darglint".

The {{ HPC }} allows one-line docstrings without function signatures.
Multi-line docstrings must
specify the function signatures completely and correctly,
using [Google docstring style].

### Bandit

[Bandit] is a tool designed to
find common security issues in Python code,
and integrated via the [flake8-bandit] extension.

[Error codes][bandit codes] are prefixed by `S` for "security".
(The prefix `B` for "bandit" is used
when Bandit is run as a stand-alone tool.)

The {{ HPC }} disables `S101` (use of assert) for the test suite,
as [pytest] uses assertions to verify expectations in tests.

(type-checking-with-mypy)=

## Type-checking with mypy

:::{note}
[Type annotations], first introduced in Python 3.5,
are a way to annotate functions and variables with types.
With appropriate tooling,
they can make your programs easier to understand, debug, and maintain.

_Type-checking_ refers to the practice of
verifying the type correctness of a program,
using type annotations and type inference.
There are two kinds of type checkers:

- _Static type checkers_ verify the type correctness of your program
  without executing it, using static analysis.
- _Runtime type checkers_ find type errors by instrumenting your code to
  type-check arguments and return values in function calls.
  This is particularly useful during the execution of unit tests.

There is also an increasing number of libraries
that leverage type annotations at runtime.
For example, you can use type annotations to generate serialization schemas
or command-line parsers.
:::

[mypy] is the pioneer and _de facto_ reference implementation of static type checking in Python.
Invoke mypy via Nox, as explained in the section {ref}`The mypy session`.

mypy is configured in the `pyproject.toml` file,
using the `tool.mypy` table. For details about supported configuration
options, see the [official reference][https://mypy.readthedocs.io/en/stable/config_file.html].

The {{ HPC }} enables several configuration options which are off by default.
The following options are enabled for strictness and enhanced output:

- {option}`strict <mypy --strict>`
- {option}`warn_unreachable <mypy --warn-unreachable>`
- {option}`pretty <mypy --pretty>`
- {option}`show_column_numbers <mypy --show-column-numbers>`
- {option}`show_error_codes <mypy --show-error-codes>`
- {option}`show_error_context <mypy --show-error-context>`

(external-services)=

## External services

Your GitHub repository can be integrated with several external services
for continuous integration and delivery.
This section describes these external services,
what they do, and how to set them up for your repository.

### PyPI

[PyPI] is the official Python Package Index.
Uploading your package to PyPI allows others to
download and install it to their system.

Follow these steps to set up PyPI for your repository:

1. Sign up at [PyPI].
2. Go to the Account Settings on PyPI,
   generate an API token, and copy it.
3. Go to the repository settings on GitHub, and
   add a secret named `PYPI_TOKEN` with the token you just copied.

PyPI is integrated with your repository
via the {ref}`Release workflow <The Release workflow>`.

### TestPyPI

[TestPyPI] is a test instance of the Python package registry.
It allows you to check your release before uploading it to the real index.

Follow these steps to set up TestPyPI for your repository:

1. Sign up at [TestPyPI].
2. Go to the Account Settings on TestPyPI,
   generate an API token, and copy it.
3. Go to the repository settings on GitHub, and
   add a secret named `TEST_PYPI_TOKEN` with the token you just copied.

TestPyPI is integrated with your repository
via the {ref}`Release workflow <The Release workflow>`.

(codecov-integration)=

### Codecov

[Codecov] is a reporting service for code coverage.

Follow these steps to set up Codecov for your repository:

1. Sign up at [Codecov].
2. Install their GitHub app.

The configuration is included in the repository,
in the file [codecov.yml][https://docs.codecov.io/docs/codecov-yaml].

Codecov integrates with your repository
via its GitHub app.
The {ref}`Tests workflow <The Tests workflow>` uploads the coverage data.

(dependabot-integration)=

### Dependabot

[Dependabot] creates pull requests with automated dependency updates.

Please refer to the [official documentation](https://docs.github.com/en/github/administering-a-repository/keeping-your-dependencies-updated-automatically) for more details.

The configuration is included in the repository,
in the file [.github/dependabot.yml](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates).

It manages the following dependencies:

```{eval-rst}
.. table::
   :widths: auto

   =================== ===================================== ================================================
   Type of dependency  Managed files                         See also
   =================== ===================================== ================================================
   Python              ``poetry.lock``                       :ref:`Managing Dependencies`
   Python              ``docs/requirements.txt``             :ref:`Read the Docs <Read the Docs integration>`
   Python              ``.github/workflows/constraints.txt`` :ref:`Workflow constraints`
   GitHub Action       ``.github/workflows/*.yml``           :ref:`GitHub Actions workflows`
   =================== ===================================== ================================================

```

(read-the-docs-integration)=

### Read the Docs

[Read the Docs] automates the building, versioning, and hosting of documentation.

Follow these steps to set up Read the Docs for your repository:

1. Sign up at [Read the Docs].
2. Import your GitHub repository,
   using the button _Import a Project_.
3. Install the GitHub [webhook](https://docs.readthedocs.io/en/stable/webhooks.html),
   using the button _Add integration_
   on the _Integrations_ tab
   in the _Admin_ section of your project
   on Read the Docs.

Read the Docs automatically starts building your documentation,
and will continue to do so when you push to the default branch or make a release.
Your documentation now has a public URL like this:

> _https://\<project>.readthedocs.io/_

The configuration for Read the Docs is included in the repository,
in the file [.readthedocs.yml](https://docs.readthedocs.io/en/stable/config-file/v2.html).
The {{ HPC }} configures Read the Docs
to build and install the package with Poetry,
using a so-called [PEP 517][pep 517]-build.

Build dependencies for the documentation
are installed using a [requirements file] located at `docs/requirements.txt`.
Read the Docs currently does not support
installing development dependencies using Poetry's lock file.
For the sake of brevity and maintainability,
only direct dependencies are included.

:::{note}
The requirements file is managed by {ref}`Dependabot <Dependabot integration>`.
When newer versions of the build dependencies become available,
Dependabot updates the requirements file and submits a pull request.
When adding or removing Sphinx extensions using Poetry,
don't forget to update the requirements file as well.
:::

(github-actions-workflows)=

## GitHub Actions workflows

The {{ HPC }} uses [GitHub Actions]
to implement continuous integration and delivery.
With GitHub Actions,
you define so-called workflows
using [YAML] files located in the `.github/workflows` directory.

A _workflow_ is an automated process
consisting of one or many jobs,
each of which executes a series of steps.
Workflows are triggered by events,
for example when a commit is pushed
or when a release is published.
You can learn more about
the workflow language and its supported keywords
in the [official reference](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/workflow-syntax-for-github-actions).

:::{note}
Real-time logs for workflow runs are available
from the _Actions_ tab in your GitHub repository.
:::

### Overview of workflows

The {{ HPC }} defines the following workflows:

```{eval-rst}
.. table:: GitHub Actions workflows
   :widths: auto

   ===================================================== ======================== ==================================== =====================
   Workflow                                              File                     Description                          Trigger
   ===================================================== ======================== ==================================== =====================
   :ref:`Tests <The Tests workflow>`                     ``tests.yml``            Run the test suite with Nox_         Push, PR
   :ref:`Release <The Release workflow>`                 ``release.yml``          Upload the package to PyPI_          Push (default branch)
   :ref:`Labeler <The Labeler workflow>`                 ``labeler.yml``          Manage GitHub project labels         Push (default branch)
   ===================================================== ======================== ==================================== =====================

```

### Overview of GitHub Actions

Workflows use the following GitHub Actions:

```{eval-rst}
.. table:: GitHub Actions
   :widths: auto

   ============================================ =========================================================
   `actions/cache`_                             Cache dependencies and build outputs
   `actions/checkout`_                          Check out the Git repository
   `actions/download-artifact`_                 Download artifacts from workflows
   `actions/setup-python`_                      Set up workflows with a specific Python version
   `actions/upload-artifact`_                   Upload artifacts from workflows
   `codecov/codecov-action`_                    Upload coverage to Codecov
   `crazy-max/ghaction-github-labeler`_         Manage labels on GitHub as code
   `pypa/gh-action-pypi-publish`_               Upload packages to PyPI and TestPyPI
   `release-drafter/release-drafter`_           Draft and publish GitHub Releases
   `salsify/action-detect-and-tag-new-version`_ Detect and tag new versions in a repository
   ============================================ =========================================================
```

:::{note}
GitHub Actions used by the workflows are managed by {ref}`Dependabot <Dependabot integration>`.
When newer versions of GitHub Actions become available,
Dependabot updates the workflows that use them and submits a pull request.
:::

(workflow-constraints)=

### Constraints file

GitHub Actions workflows install the following tools:

- [pip]
- [virtualenv]
- [Poetry]
- [Nox]

These dependencies are pinned using a [constraints file]
located in `.github/workflow/constraints.txt`.

:::{note}
The constraints file is managed by {ref}`Dependabot <Dependabot integration>`.
When newer versions of the tools become available,
Dependabot updates the constraints file and submits a pull request.
:::

(the-tests-workflow)=

### The Tests workflow

The Tests workflow runs checks using Nox.
It is triggered on every push to the repository,
and when a pull request is opened or receives new commits.

Each Nox session runs in a separate job,
using the current release of Python
and the [latest Ubuntu runner](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/virtual-environments-for-github-hosted-runners#supported-runners-and-hardware-resources).
Selected Nox sessions also run on Windows and macOS,
and with older Python versions,
as shown in the table below:

```{eval-rst}
.. table:: Jobs in the Tests workflow
   :widths: auto

   ========================================== ====================== ==================
   Nox session                                Platform               Python versions
   ========================================== ====================== ==================
   :ref:`pre-commit <The pre-commit session>` Ubuntu                 3.10
   :ref:`safety <The safety session>`         Ubuntu                 3.10
   :ref:`mypy <The mypy session>`             Ubuntu                 3.10, 3.9, 3.8, 3.7
   :ref:`tests <The tests session>`           Ubuntu                 3.10, 3.9, 3.8, 3.7
   :ref:`tests <The tests session>`           Windows                3.10
   :ref:`tests <The tests session>`           macOS                  3.10
   :ref:`coverage <The coverage session>`     Ubuntu                 3.10
   :ref:`docs-build <The docs-build session>` Ubuntu                 3.10
   ========================================== ====================== ==================
```

The workflow uploads the generated documentation as a [workflow artifact](https://help.github.com/en/actions/configuring-and-managing-workflows/persisting-workflow-data-using-artifacts).
Building the documentation only serves the purpose of catching issues in pull requests.
Builds on [Read the Docs] happen independently.

The workflow also uploads coverage data to [Codecov] after running tests.
It generates a coverage report in [Cobertura](https://cobertura.github.io/cobertura/) XML format,
using the {ref}`coverage session <The coverage session>`.
The report is uploaded
using the official [Codecov GitHub Action][codecov/codecov-action].

The Tests workflow uses the following GitHub Actions:

- [actions/checkout] for checking out the Git repository
- [actions/setup-python] for setting up the Python interpreter
- [actions/download-artifact] to download the coverage data of each tests session
- [actions/cache] for caching pre-commit environments
- [actions/upload-artifact] to upload the generated documentation and the coverage data of each tests session
- [codecov/codecov-action] for uploading to [Codecov]

The Tests workflow is defined in `.github/workflows/tests.yml`.

(the-release-workflow)=

### The Release workflow

The Release workflow publishes your package on [PyPI], the Python Package Index.
The workflow also creates a version tag in the GitHub repository,
and publishes a GitHub Release using [Release Drafter].
The workflow is triggered on every push to the default branch.

Release steps only run if the package version was bumped.
If the package version did not change,
the package is instead uploaded to [TestPyPI] as a prerelease,
and only a draft GitHub Release is created.
TestPyPI is a test instance of the Python Package Index.

The Release workflow uses API tokens to access [PyPI] and [TestPyPI].
You can generate these tokens from your account settings on these services.
The tokens need to be stored as secrets in the repository settings on GitHub:

```{eval-rst}
.. table:: Secrets
   :widths: auto

   =================== ===================
   ``PYPI_TOKEN``      PyPI_ API token
   ``TEST_PYPI_TOKEN`` TestPyPI_ API token
   =================== ===================
```

The Release workflow uses the following GitHub Actions:

- [actions/checkout] for checking out the Git repository
- [actions/setup-python] for setting up the Python interpreter
- [salsify/action-detect-and-tag-new-version] for tagging on version bumps
- [pypa/gh-action-pypi-publish] for uploading the package to PyPI or TestPyPI
- [release-drafter/release-drafter] for publishing the GitHub Release

Release notes are populated with the titles and authors of merged pull requests.
You can group the pull requests into separate sections
by applying labels to them, like this:

```{eval-rst}
.. include:: quickstart.md
   :parser: myst_parser.sphinx_
   :start-after: <!-- table-release-drafter-sections-begin -->
   :end-before: <!-- table-release-drafter-sections-end -->
```

The workflow is defined in `.github/workflows/release.yml`.
The Release Drafter configuration is located in `.github/release-drafter.yml`.

(the-labeler-workflow)=

### The Labeler workflow

The Labeler workflow manages the labels used in GitHub issues
and pull requests based on a description file `.github/labels.yaml`.
In this file each label is described with
a `name`,
a `description`
and a `color`.
The workflow is triggered on every push to the default branch.

The workflow creates or updates project labels if they are missing
or different compared to the `labels.yml` file content.

The workflow does not delete labels already configured in the GitHub UI
and not in the `labels.yml` file.
You can change this behavior and add ignore patterns
in the settings of the workflow (see [GitHub Labeler] documentation).

The Labeler workflow uses the following GitHub Actions:

- [actions/checkout] for checking out the Git repository
- [crazy-max/ghaction-github-labeler] for updating the GitHub project labels

The workflow is defined in `.github/workflows/labeler.yml`.
The GitHub Labeler configuration is located in `.github/labels.yml`.

(tutorials)=

## Tutorials

First, make sure you have all the {ref}`requirements <Installation>` installed.

(how-to-test-your-project)=

### How to test your project

Run the test suite using {ref}`Nox <Using Nox>`:

```console
$ nox -r
```

### How to run your code

First, install the project and its dependencies to the Poetry environment:

```console
$ poetry install
```

Run an interactive session in the environment:

```console
$ poetry run python
```

Invoke the command-line interface of your package:

```console
$ poetry run <project>
```

### How to make code changes

1. Run the tests,
   {ref}`as explained above <How to test your project>`.<br>
   All tests should pass.
2. Add a failing test
   {ref}`under the tests directory <The test suite>`.<br>
   Run the tests again to verify that your test fails.
3. Make your changes to the package,
   {ref}`under the src directory <The initial package>`.<br>
   Run the tests to verify that all tests pass again.

### How to push code changes

Create a branch for your changes:

```console
$ git switch --create my-topic-branch main
```

Create a series of small, single-purpose commits:

```console
$ git add <files>
$ git commit
```

Push your branch to GitHub:

```console
$ git push --set-upstream origin my-topic-branch
```

The push triggers the following automated steps:

- {ref}`The test suite runs against your branch <The Tests workflow>`.

### How to open a pull request

Open a pull request for your branch on GitHub:

1. Select your branch from the _Branch_ menu.
2. Click **New pull request**.
3. Enter the title for the pull request.
4. Enter a description for the pull request.
5. Apply a {ref}`label identifying the type of change <The Release workflow>`
6. Click **Create pull request**.

Release notes are pre-filled with the titles of merged pull requests.

### How to accept a pull request

If all checks are marked as passed,
merge the pull request using the squash-merge strategy (recommended):

1. Click **Squash and Merge**.
   (Select this option from the dropdown menu of the merge button, if it is not shown.)
2. Click **Confirm squash and merge**.
3. Click **Delete branch**.

This triggers the following automated steps:

- {ref}`The test suite runs against the main branch <The Tests workflow>`.
- {ref}`The draft GitHub Release is updated <The Release workflow>`.
- {ref}`A pre-release of the package is uploaded to TestPyPI <The Release workflow>`.
- [Read the Docs] rebuilds the _latest_ version of the documentation.

In your local repository,
update the main branch:

```console
$ git switch main
$ git pull origin main
```

Optionally, remove the merged topic branch
from the local repository as well:

```console
$ git remote prune origin
$ git branch --delete --force my-topic-branch
```

The original commits remain accessible from the pull request
(_Commits_ tab).

### How to make a release

Releases are triggered by a version bump on the default branch.
It is recommended to do this in a separate pull request:

1. Switch to a branch.
2. Bump the version using [poetry version].
3. Commit and push to GitHub.
4. Open a pull request.
5. Merge the pull request.

The individual steps for bumping the version are:

```console
$ git switch --create release main
$ poetry version <version>
$ git commit --message="<project> <version>" pyproject.toml
$ git push origin release
```

If you're not sure which version number to choose,
read about [Semantic Versioning].
Versioning rules for Python packages are laid down in [PEP 440][pep 440].

Before merging the pull request for the release,
go through the following checklist:

- The pull request passes all checks.
- The development release on [TestPyPI] looks good.
- All pull requests for the release have been merged.

Merging the pull request triggers the
{ref}`Release workflow <The Release workflow>`.
This workflow performs the following automated steps:

- Publish the package on PyPI.
- Publish a GitHub Release.
- Apply a Git tag to the repository.

[Read the Docs] automatically builds a new stable version of the documentation.

## The Hypermodern Python blog

The project setup is described in detail in the [Hypermodern Python] article series:

- [Chapter 1: Setup](https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769)
- [Chapter 2: Testing](https://medium.com/@cjolowicz/hypermodern-python-2-testing-ae907a920260)
- [Chapter 3: Linting](https://medium.com/@cjolowicz/hypermodern-python-3-linting-e2f15708da80)
- [Chapter 4: Typing](https://medium.com/@cjolowicz/hypermodern-python-4-typing-31bcf12314ff)
- [Chapter 5: Documentation](https://medium.com/@cjolowicz/hypermodern-python-5-documentation-13219991028c)
- [Chapter 6: CI/CD](https://medium.com/@cjolowicz/hypermodern-python-6-ci-cd-b233accfa2f6)

You can also read the articles on [this blog](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/).

[--reuse-existing-virtualenvs]: https://nox.thea.codes/en/stable/usage.html#re-using-virtualenvs
[.gitattributes]: https://git-scm.com/book/en/Customizing-Git-Git-Attributes
[.gitignore]: https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_ignoring
[2021.11.26]: https://github.com/cjolowicz/cookiecutter-hypermodern-python/releases/tag/2021.11.26
[actions/cache]: https://github.com/actions/cache
[actions/checkout]: https://github.com/actions/checkout
[actions/download-artifact]: https://github.com/actions/download-artifact
[actions/setup-python]: https://github.com/actions/setup-python
[actions/upload-artifact]: https://github.com/actions/upload-artifact
[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[bandit]: https://github.com/PyCQA/bandit
[bandit codes]: https://bandit.readthedocs.io/en/latest/plugins/index.html#complete-test-plugin-listing
[bash]: https://www.gnu.org/software/bash/
[black]: https://github.com/psf/black
[calendar versioning]: https://calver.org
[check-added-large-files]: https://github.com/pre-commit/pre-commit-hooks#check-added-large-files
[check-toml]: https://github.com/pre-commit/pre-commit-hooks#check-toml
[check-yaml]: https://github.com/pre-commit/pre-commit-hooks#check-yaml
[click]: https://click.palletsprojects.com/
[click.testing.clirunner]: https://click.palletsprojects.com/en/7.x/testing/
[codecov]: https://codecov.io/
[codecov/codecov-action]: https://github.com/codecov/codecov-action
[constraints file]: https://pip.pypa.io/en/stable/user_guide/#constraints-files
[contributor covenant]: https://www.contributor-covenant.org
[cookiecutter]: https://github.com/audreyr/cookiecutter
[coverage.py]: https://coverage.readthedocs.io/
[crazy-max/ghaction-github-labeler]: https://github.com/crazy-max/ghaction-github-labeler
[cupper]: https://github.com/senseyeio/cupper
[curl]: https://curl.haxx.se
[cyclomatic complexity]: https://en.wikipedia.org/wiki/Cyclomatic_complexity
[darglint]: https://github.com/terrencepreilly/darglint
[darglint codes]: https://github.com/terrencepreilly/darglint#error-codes
[dependabot]: https://dependabot.com/
[dependabot issue 4435]: https://github.com/dependabot/dependabot-core/issues/4435
[dev-prod parity]: https://12factor.net/dev-prod-parity
[end-of-file-fixer]: https://github.com/pre-commit/pre-commit-hooks#end-of-file-fixer
[flake8]: http://flake8.pycqa.org
[flake8-bandit]: https://github.com/tylerwince/flake8-bandit
[flake8-bugbear]: https://github.com/PyCQA/flake8-bugbear
[flake8-bugbear codes]: https://github.com/PyCQA/flake8-bugbear#list-of-warnings
[flake8-docstrings]: https://gitlab.com/pycqa/flake8-docstrings
[flake8-rst-docstrings]: https://github.com/peterjc/flake8-rst-docstrings
[flake8-rst-docstrings codes]: https://github.com/peterjc/flake8-rst-docstrings#flake8-validation-codes
[furo]: https://pradyunsg.me/furo/
[git]: https://www.git-scm.com
[git hook]: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
[github]: https://github.com/
[github actions]: https://github.com/features/actions
[github labeler]: https://github.com/marketplace/actions/github-labeler
[github release]: https://help.github.com/en/github/administering-a-repository/about-releases
[google docstring style]: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
[hypermodern python]: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[install-poetry.py]: https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py
[isort]: https://pycqa.github.io/isort/
[jinja]: https://palletsprojects.com/p/jinja/
[json]: https://www.json.org/
[markdown]: https://spec.commonmark.org/current/
[mccabe]: https://github.com/PyCQA/mccabe
[mccabe codes]: https://github.com/PyCQA/mccabe#plugin-for-flake8
[mit license]: https://opensource.org/licenses/MIT
[mypy]: http://mypy-lang.org/
[myst]: https://myst-parser.readthedocs.io/
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[nox]: https://nox.thea.codes/
[nox-poetry]: https://nox-poetry.readthedocs.io/
[package metadata]: https://packaging.python.org/en/latest/specifications/core-metadata/
[pep 257]: http://www.python.org/dev/peps/pep-0257/
[pep 440]: https://www.python.org/dev/peps/pep-0440/
[pep 517]: https://www.python.org/dev/peps/pep-0517/
[pep 518]: https://www.python.org/dev/peps/pep-0518/
[pep 561]: https://www.python.org/dev/peps/pep-0561/
[pep 8]: http://www.python.org/dev/peps/pep-0008/
[pep8-naming]: https://github.com/pycqa/pep8-naming
[pep8-naming codes]: https://github.com/pycqa/pep8-naming#pep-8-naming-conventions
[pip]: https://pip.pypa.io/
[pip install]: https://pip.pypa.io/en/stable/reference/pip_install/
[pipx]: https://pipxproject.github.io/pipx/
[poetry]: https://python-poetry.org/
[poetry add]: https://python-poetry.org/docs/cli/#add
[poetry env]: https://python-poetry.org/docs/managing-environments/
[poetry export]: https://python-poetry.org/docs/cli/#export
[poetry install]: https://python-poetry.org/docs/cli/#install
[poetry remove]: https://python-poetry.org/docs/cli/#remove
[poetry run]: https://python-poetry.org/docs/cli/#run
[poetry show]: https://python-poetry.org/docs/cli/#show
[poetry update]: https://python-poetry.org/docs/cli/#update
[poetry version]: https://python-poetry.org/docs/cli/#version
[pre-commit]: https://pre-commit.com/
[pre-commit-hooks]: https://github.com/pre-commit/pre-commit-hooks
[prettier]: https://prettier.io/
[pycodestyle]: https://pycodestyle.pycqa.org/en/latest/
[pycodestyle codes]: https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes
[pydocstyle]: http://www.pydocstyle.org/
[pydocstyle codes]: http://www.pydocstyle.org/en/stable/error_codes.html
[pyenv]: https://github.com/pyenv/pyenv
[pyflakes]: https://github.com/PyCQA/pyflakes
[pyflakes codes]: https://flake8.pycqa.org/en/latest/user/error-codes.html
[pygments]: https://pygments.org/
[pypa/gh-action-pypi-publish]: https://github.com/pypa/gh-action-pypi-publish
[pypi]: https://pypi.org/
[pyproject.toml]: https://python-poetry.org/docs/pyproject/
[pytest]: https://docs.pytest.org/en/latest/
[python build]: https://python-poetry.org/docs/cli/#build
[python package]: https://docs.python.org/3/tutorial/modules.html#packages
[python publish]: https://python-poetry.org/docs/cli/#publish
[pyupgrade]: https://github.com/asottile/pyupgrade
[read the docs]: https://readthedocs.org/
[release drafter]: https://github.com/release-drafter/release-drafter
[release-drafter/release-drafter]: https://github.com/release-drafter/release-drafter
[requirements file]: https://pip.readthedocs.io/en/stable/user_guide/#requirements-files
[restructuredtext]: https://docutils.sourceforge.io/rst.html
[safety]: https://github.com/pyupio/safety
[salsify/action-detect-and-tag-new-version]: https://github.com/salsify/action-detect-and-tag-new-version
[semantic versioning]: https://semver.org/
[sphinx]: http://www.sphinx-doc.org/
[sphinx-autobuild]: https://github.com/executablebooks/sphinx-autobuild
[sphinx-click]: https://sphinx-click.readthedocs.io/
[test fixture]: https://docs.pytest.org/en/latest/explanation/fixtures.html#about-fixtures
[testpypi]: https://test.pypi.org/
[toml]: https://github.com/toml-lang/toml
[tox]: https://tox.readthedocs.io/
[trailing-whitespace]: https://github.com/pre-commit/pre-commit-hooks#trailing-whitespace
[type annotations]: https://docs.python.org/3/library/typing.html
[typeguard]: https://github.com/agronholm/typeguard
[versions and constraints]: https://python-poetry.org/docs/dependency-specification/
[virtual environment]: https://docs.python.org/3/tutorial/venv.html
[virtualenv]: https://virtualenv.pypa.io/
[wheel]: https://www.python.org/dev/peps/pep-0427/
[xdoctest]: https://github.com/Erotemic/xdoctest
[yaml]: https://yaml.org/
