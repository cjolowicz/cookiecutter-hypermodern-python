User Guide
==========

This is the user guide 
for the `Hypermodern Python Cookiecutter`_,
a Python template based on the `Hypermodern Python`_ article series.

If you're in a hurry, check out the :doc:`quickstart guide <quickstart>`
and the :ref:`tutorials <Tutorials>`.

.. contents::
    :local:
    :backlinks: none


Introduction
~~~~~~~~~~~~

About this project
------------------

The *Hypermodern Python Cookiecutter* is
a general-purpose template for Python libraries and applications,
released under the `MIT license`_
and hosted on `GitHub <Hypermodern Python Cookiecutter_>`__.

The main objective of this project template is to
enable current best practises
through modern Python tooling.
Our goals are to:

- keep a focus on simplicity and minimalism,
- promote code quality through automation, and
- provide reliable and repeatable processes,

all the way from local testing to publishing releases.

Projects are created from the template using Cookiecutter_,
a project scaffolding tool built on top of the Jinja_ template engine.

The project template is centered around the following tools:

- Poetry_ for packaging and dependency management
- Nox_ for automation of checks and other development tasks
- `GitHub Actions`_ for continuous integration and delivery


.. _Features:

Features
--------

Here is a detailed list of features for this Python template:

.. include:: ../README.rst
   :start-after: features-begin
   :end-before: features-end


Release cadence
---------------

The *Hypermodern Python Cookiecutter* has a `bimonthly`_ release cadence.
Releases happen on the 15th of every other month, starting in January.
We use `Calendar Versioning`_ with a ``YYYY.MM.DD`` versioning scheme.
Initial releases may occur more frequently.

.. _`bimonthly`: https://www.merriam-webster.com/words-at-play/on-biweekly-and-bimonthly

The current stable release is `2020.4.15.1`_.

.. _`2020.4.15.1`: https://github.com/cjolowicz/cookiecutter-hypermodern-python/releases/tag/2020.4.15.1


Installation
~~~~~~~~~~~~

System requirements
-------------------

You need a recent Linux, Unix, or Mac system with
bash_, curl_, and git_.

On Windows 10, enable the `Windows Subsystem for Linux`_ (WSL) and
install the Ubuntu 18.04 LTS distribution.
Open Ubuntu from the Start Menu, and
install additional packages using the following commands:

.. _`Windows Subsystem for Linux`: https://docs.microsoft.com/en-us/windows/wsl/install-win10

.. code:: console

   $ sudo apt update
   $ sudo apt install -y build-essential curl git libbz2-dev \
     libffi-dev liblzma-dev libncurses5-dev libncursesw5-dev \
     libreadline-dev libsqlite3-dev libssl-dev llvm make \
     python-openssl tk-dev wget xz-utils zlib1g-dev

The project template should also work natively on Windows.
Pull requests to document Windows specifics are welcome!

.. note::

   When working with this template on Windows,
   configure your text editor or IDE
   to use only `UNIX-style line endings`__ (line feeds).

   __ https://en.wikipedia.org/wiki/Newline

   The project template contains a `.gitattributes`__ file
   which enables end-of-line normalization for your entire working tree.
   Additionally, the Prettier_ code formatter converts line endings to line feeds.
   Windows-style line endings (`CRLF`) should therefore never make it into your Git repository.

   __ https://git-scm.com/book/en/Customizing-Git-Git-Attributes

   Nonetheless, configuring your editor for line feeds is recommended
   to avoid complaints from the pre-commit_ hook for Prettier.


Getting Python
--------------

It is recommended to use pyenv_ for
installing and managing Python versions.
Please refer to the documentation of this project
for detailed installation and usage instructions.

Install pyenv_ like this:

.. code:: console

   $ curl https://pyenv.run | bash

Add the following lines to your ``~/.bashrc``:

.. code:: sh

   export PATH="$HOME/.pyenv/bin:$PATH"
   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"

Install the Python build dependencies for your platform,
using one of the commands listed in the
`official instructions <pyenv wiki_>`__.

.. _`pyenv wiki`: https://github.com/pyenv/pyenv/wiki/Common-build-problems

Install the latest point release of every supported Python version.
This project template supports Python 3.6, 3.7, and 3.8.

.. code:: console

   $ pyenv install 3.6.10
   $ pyenv install 3.7.7
   $ pyenv install 3.8.2

After creating your project (see :ref:`below <Creating a project>`),
you can make these Python versions accessible in the project directory,
using the following command:

.. code:: console

   $ pyenv local 3.8.2 3.7.7 3.6.10

The first version listed is the one used when you type plain ``python``.
Every version can be used by invoking ``python<major.minor>``.
For example, use ``python3.7`` to invoke Python 3.7.


Requirements
------------

.. note::

   It is recommended to use pipx_ to install Python tools
   which are not specific to a single project.
   Please refer to the official documentation
   for detailed installation and usage instructions.
   If you decide to skip ``pipx`` installation,
   use `pip install`_ with the ``--user`` option instead.

You only need three tools to use this template:

- Cookiecutter_ to create projects from the template,
- Poetry_ to manage packaging and dependencies
- Nox_ to automate checks and other tasks

As an optional requirement,
pre-commit_ is recommended for additional checks and to manage Git hooks.

Install Cookiecutter_ using pipx:

.. code:: console

   $ pipx install cookiecutter

Install Poetry_ by downloading and running get-poetry.py_:

.. _`get-poetry.py`: https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py

.. code:: console

   $ python get-poetry.py

Install Nox_ using pipx:

.. code:: console

   $ pipx install nox

Install pre-commit_ using pipx:

.. code:: console

   $ pipx install pre-commit


Project creation
~~~~~~~~~~~~~~~~

.. _`Creating a project`:

Creating a project
------------------

Create a project from this template
by pointing Cookiecutter to its `GitHub repository <Hypermodern Python Cookiecutter_>`__.
Use the ``--checkout`` option with the `current stable release <2020.4.15.1_>`__:

.. code:: console

   $ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python \
     --checkout="2020.4.15.1"

Cookiecutter downloads the template,
and asks you a series of questions about project variables,
for example, how you wish your project to be named.
When you have answered these questions,
your project is generated in the current directory,
using a subdirectory with the same name as your project.

Here is a complete list of the project variables defined by this template:

================== =============================== ======================
Project Variable   Description                     Example
================== =============================== ======================
``project_name``   Project name on PyPI and GitHub ``hypermodern-python``
``package_name``   Import name of the package      ``hypermodern_python``
``friendly_name``  Friendly project name           ``Hypermodern Python``
``author``         Primary author                  Jane Doe
``email``          E-mail address of the author    jane.doe@example.com
``github_user``    GitHub username of the author   ``janedoe``
``version``        Initial project version         ``0.1.0``
================== =============================== ======================

In the remainder of this guide,
``<project>`` and ``<package>`` are used
to refer to the project and package names, respectively.


The initial package
-------------------

You can find the initial Python package in your generated project
under the ``src`` directory::

  src
  └── <package>
      ├── __init__.py
      ├── __main__.py
      └── py.typed

``__init__.py``
   This file declares the directory as a `Python package`_.

   .. _`Python package`: https://docs.python.org/3/tutorial/modules.html#packages

``__main__.py``
   This module defines the ``__main__.main`` entry point
   for the command-line interface.
   The command-line interface is implemented using Click_,
   and supports ``--help`` and ``--version`` options.
   When the package is installed,
   a script named ``<project>`` is placed
   in the ``bin`` directory of the Python installation or virtual environment,
   allowing you to invoke the command-line interface
   like any other console application.
   The command-line interface can also be invoked
   by specifying a Python interpreter and the package name:

   .. code:: console

      $ python -m <package> [<options>]

``py.typed``
   This is an empty marker file,
   which declares that your package supports typing
   and is distributed with its own type information
   (`PEP 561`_).
   This allows people using your package
   to type-check their Python code against it.
 

Uploading to GitHub
-------------------

This project template is designed for use with GitHub_,
so your next steps are to create a Git repository and upload it to GitHub.

Change to the root directory of your new project,
initialize a Git repository, and
create a commit for the initial project structure:

.. code:: console

   $ git init
   $ git add .
   $ git commit

Create an empty repository on GitHub_,
using the project name you chose when you generated the project.
Do not include a ``README.md``, ``LICENSE``, or ``.gitignore``.
These files are provided by the project template.

Finally, upload your repository to GitHub.
In the commands below, replace ``<username>`` by your GitHub username,
and ``<repository>`` by the name of your GitHub repository.

.. code:: console

   $ git remote add origin git@github.com:<username>/<repository>.git
   $ git push --set-upstream origin master


Packaging
~~~~~~~~~

The pyproject.toml file
-----------------------

The configuration file for the Python package is located
in the root directory of the project,
and named ``pyproject.toml``.
It uses the TOML_ configuration file format,
and contains two sections---*tables* in TOML parlance---,
specified in `PEP 517`_ and `518 <PEP 518_>`__:

- The ``build-system`` table
  declares the requirements and the entry point
  used to build a distribution package for the project.
  This template uses Poetry_ as the build system.
- The ``tool`` table contains sub-tables
  where tools can store configuration under their PyPI_ name.
  Poetry stores its configuration in the ``tool.poetry`` table.

The ``tool.poetry`` table
contains the metadata for your package,
such as its name, version, and authors,
as well as the list of dependencies for the package.
Please refer to the `Poetry documentation <pyproject.toml_>`__
for a detailed description of each configuration key.

.. _`pyproject.toml`: https://python-poetry.org/docs/pyproject/


Building and distributing the package
-------------------------------------

.. note::

   With the *Hypermodern Python Cookiecutter*,
   building and distributing your package
   is taken care of by `GitHub Actions`_
   when you publish a `GitHub Release`_.

This section gives a short overview of
how you can build and distribute your package
from the command line,
using the following Poetry commands:

.. code:: console

   $ poetry build
   $ poetry publish

Building the package is done with the `python build`_ command.
This command generates *distribution packages*
in the ``dist`` directory of your project.
These are compressed archives which
an end-user can download and install on their system.
They come in two flavours:
source (or *sdist*) archives, and 
binary packages in the wheel_ format.

Publishing the package is done with the `python publish`_ command.
This command uploads the distribution packages
to your account on PyPI_,
the official Python package registry.

.. _`python build`: https://python-poetry.org/docs/cli/#build
.. _`python publish`: https://python-poetry.org/docs/cli/#publish
.. _`wheel`: https://www.python.org/dev/peps/pep-0427/ 


Installing the package
----------------------

With your package on PyPI,
others can install it with pip_, pipx_, or Poetry:

.. code:: console

   $ pip install <project>
   $ pipx install <project>
   $ poetry add <project>

While pip_ is the workhorse of the Python packaging ecosystem,
you should normally use higher-level tools to install your package:

- If the package is an application, install it with pipx_.
- If the package is a library, install it with `poetry add`_ in other projects.

The primary benefit of these installation methods is that
your package is installed into an isolated environment,
without polluting the system environment,
or the environments of other applications.
This way,
applications can use specific versions of their direct and indirect dependencies,
without getting in each other's way.

.. _`poetry add`: https://python-poetry.org/docs/cli/#add

If the other project is not managed by Poetry,
use whatever package manager the other project uses.
You can always install your project into a virtual environment with plain pip_.


Dependencies
~~~~~~~~~~~~

Types of dependencies
---------------------

Dependencies are Python packages used by your project,
and they come in two types:

- *Core dependencies* are required by users running your code,
  and typically consist of third-party libraries imported by your package.
  These dependencies are also declared in distribution packages such as wheels,
  allowing tools like pip_ to automatically install them alongside your package.

- *Development dependencies* are only required by developers working on your code.
  Examples are applications used to run tests,
  check code for style and correctness,
  or to build documentation.
  These dependencies are not a part of distribution packages,
  because users do not require them to run your code.

This project template has a core dependency on Click_,
a library for creating command-line interfaces

The project template also comes with a large number of development dependencies.
See :ref:`features` for an overview.


Managing dependencies
---------------------

Use the command `poetry show`_ to
see the full list of direct and indirect dependencies of your package:

.. code:: console

   $ poetry show

.. _`poetry show`: https://python-poetry.org/docs/cli/#show

Use the command `poetry add`_ to add a dependency for your package:

.. code:: console

   $ poetry add foobar        # for core dependencies
   $ poetry add --dev foobar  # for development dependencies 

Use the command `poetry remove`_ to remove a dependency from your package:

.. code:: console

   $ poetry remove foobar

.. _`poetry remove`: https://python-poetry.org/docs/cli/#remove

Use the command `poetry update`_ to upgrade the dependency to a new release:

.. code:: console

   $ poetry update foobar

.. _`poetry update`: https://python-poetry.org/docs/cli/#update

To upgrade to a new major release,
you normally need to update the version constraint for the dependency,
in the ``pyproject.toml`` file.


Version constraints
-------------------

`Version constraints`_ express which versions of dependencies are compatible with your project.
In the case of core dependencies,
they are also a part of distribution packages,
and as such affect end-users of your package.

For every dependency added to your project,
Poetry writes a version constraint to ``pyproject.toml``.
Dependencies are kept in two TOML tables:

- ``tool.poetry.dependencies``---for core dependencies
- ``tool.poetry.dev-dependencies``---for development dependencies

By default, version constraints require users to have at least
the version of a dependency that was current when you added it to the project.
Users can also upgrade to newer releases of dependencies,
as long as the version number does not indicate a breaking change.
(After 1.0.0, `Semantic Versioning`_ limits breaking changes to major releases.)

.. _`version constraint`: https://python-poetry.org/docs/versions/
.. _`Semantic Versioning`: https://semver.org/


The lock file
-------------

Poetry records the exact version of each direct and indirect dependency
in its lock file, named ``poetry.lock`` and located in the root directory of the project.
The lock file does not affect users of the package,
because its contents are not included in distribution packages.

The lock file is useful for a number of reasons:

- It ensures that local checks run in the same environment as on the CI server,
  making the CI predictable and deterministic.
- When collaborating with other developers,
  it allows everybody to use the same development environment.
- When deploying an application, the lock file helps you
  keep production and development environments as similar as possible
  (`dev-prod parity`_).

.. _`dev-prod parity`: https://12factor.net/dev-prod-parity

For these reasons, the lock file should be kept under source control.


The Poetry environment
~~~~~~~~~~~~~~~~~~~~~~

Poetry manages a `virtual environment`_ for your project,
containing your package together with its core dependencies,
as well as the development dependencies.
All dependencies are kept at the versions specified by the lock file.

A virtual environment gives your project
an isolated runtime environment,
consisting of a specific Python version and
an independent set of installed Python packages.
This way, the dependencies of your current project
do not interfere with the system-wide Python installation,
or other projects you're working on.

.. _`virtual environment`: https://docs.python.org/3/tutorial/venv.html


Installing the package for development
--------------------------------------

You can install your package and its dependencies
into Poetry's virtual environment
using the command `poetry install`_.

.. code:: console

   $ poetry install

.. _`poetry install`: https://python-poetry.org/docs/cli/#install

This command performs a so-called `editable install`_ of your package:
Instead of building and installing a distribution package,
it creates a special ``.egg-link`` file that links to your local source code.
This means that code edits are directly visible in the environment
without the need to reinstall your package.

.. _`editable install`: https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs

Installing your package implicitly creates the virtual environment 
if it does not exist yet,
using the currently active Python interpreter,
or the first one found
which satisfies the Python versions supported by your project.


Managing environments
---------------------

You can create environments explicitly
with the `poetry env`_ command,
specifying the desired Python version.
This allows you to create an environment
for every Python version supported by your project,
and easily switch between them:

.. _`poetry env`: https://python-poetry.org/docs/managing-environments/

.. code:: console

   $ poetry env use 3.6
   $ poetry env use 3.7
   $ poetry env use 3.8

Only one Poetry environment can be active at any time.
Note that ``3.8`` comes last,
to ensure that the current Python release is the active environment.
Install your package with ``poetry install`` into each environment after creating it.

Use the command ``poetry env list`` to list the available environments:

.. code:: console

   $ poetry env list

Use the command ``poetry env remove`` to remove an environment:

.. code:: console

   $ poetry env remove <version>

Use the command ``poetry env info`` to show information about the active environment:

.. code:: console

   $ poetry env info


Running commands
----------------

You can run an interactive Python session inside the active environment
using the command `poetry run`_:

.. _`poetry run`: https://python-poetry.org/docs/cli/#run

.. code:: console

   $ poetry run python

The same command allows you to invoke the command-line interface of your project:

.. code:: console

   $ poetry run <project>

You can also run developer tools, such as pytest_:

.. code:: console

   $ poetry run pytest

While it is handy to have developer tools available in the Poetry environment,
it is usually recommended to run these using Nox_,
as described in the :ref:`next <Using Nox>` section.


.. _`Using Nox`:

Using Nox
~~~~~~~~~

Nox_ automates testing in multiple Python environments.
Like its older sibling tox_,
Nox makes it easy to run any kind of job in an isolated environment,
with only those dependencies installed that the job needs.
Nox sessions are defined in a Python file
named ``noxfile.py`` and located in the project directory.
They consist of a virtual environment
and a set of commands to run in that environment.

.. _`tox`: https://tox.readthedocs.io/

While Poetry environments allow you to
interact with your package during development,
Nox environments are used to run developer tools
in a reliable and repeatable way across Python versions.
Most sessions are run with every supported Python version.
Other sessions are only run with the current stable Python version,
for example the session used to build the documentation.


Running sessions
----------------

If you invoke Nox by itself, it will run the full test suite:

.. code:: console

   $ nox

This includes unit tests, linters, and type checkers,
but excludes sessions like those for building documentation or for reformatting code.
The list of sessions run by default can be configured
by editing ``nox.options.sessions`` in ``noxfile.py``.

You can also run a specific Nox session, using the ``--session`` option.
For example, build the documentation like this:

.. code:: console

   $ nox --session=docs

Print a list of the available Nox sessions
using the ``--list-sessions`` option:

.. code:: console

   $ nox --list-sessions

Nox creates virtual environments from scratch on each invocation
(a sensible default).
You can speed things up by passing the
`--reuse-existing-virtualenvs`_ option
(or the equivalent short option ``-r``):

.. code:: console

   $ nox --reuse-existing-virtualenvs

.. _`--reuse-existing-virtualenvs`: https://nox.thea.codes/en/stable/usage.html#re-using-virtualenvs


Available sessions
------------------

.. _`Table of Nox sessions`:

The following tables gives an overview of the available Nox sessions:

====================================== ============================== ================== =========
Session                                Description                    Python              Default
====================================== ============================== ================== =========
`black <The black session_>`__         Format code with Black_        ``3.8``
`docs <The docs session_>`__           Build Sphinx_ documentation    ``3.8``
`lint <The lint session_>`__           Lint with Flake8_              ``3.6`` … ``3.8``      ✓
`mypy <The mypy session_>`__           Type-check with mypy_          ``3.6`` … ``3.8``      ✓
`safety <The safety session_>`__       Scan dependencies with Safety_ ``3.8``                ✓
`tests <The tests session_>`__         Run tests with pytest_         ``3.6`` … ``3.8``      ✓
`typeguard <The typeguard session_>`__ Type-check with Typeguard_     ``3.6`` … ``3.8``
`xdoctest <The xdoctest session_>`__   Run examples with xdoctest_    ``3.6`` … ``3.8``
====================================== ============================== ================== =========



Using Poetry inside Nox sessions
--------------------------------

Nox sessions can invoke Poetry like any other command,
using the function `nox.sessions.Session.run`_.
Integrating Nox and Poetry in a sane way requires additional work.
For this purpose, ``noxfile.py`` contains some glue code
in the form of the ``install`` and ``install_package`` functions,
and the ``Poetry`` helper class.

.. _`nox.sessions.Session.run`: https://nox.thea.codes/en/stable/config.html#nox.sessions.Session.run

``noxfile.install(session, *args)``:
   Install dependencies into a Nox session using Poetry.

The ``noxfile.install`` function
installs development dependencies into a Nox session,
using the versions specified in Poetry's lock file.
This is done by exporting the lock file in ``requirements.txt`` format,
and passing it as a `constraints file`_ to pip.
The function arguments are the same as those for `nox.sessions.Session.install`_:
The first argument is the ``Session`` object,
and the remaining arguments are command-line arguments for `pip install`_,
typically just the package or packages to be installed.

.. _`nox.sessions.Session.install`: https://nox.thea.codes/en/stable/config.html#nox.sessions.Session.install
.. _`constraints file`: https://pip.pypa.io/en/stable/user_guide/#constraints-files
.. _`pip install`: https://pip.pypa.io/en/stable/reference/pip_install/

``noxfile.install_package(session)``:
   Install the package into a Nox session using Poetry.

The ``noxfile.install_package`` function
installs your package into a Nox session,
including the core dependencies as specified in Poetry's lock file.
This is done by building a wheel from the package,
and installing it using pip_.
Dependencies are installed in the same way as in the ``noxfile.install`` function,
i.e. using a constraints file.
Its only argument is the ``Session`` object from Nox.

The functions are implemented using a ``Poetry`` helper class,
encapsulating invocations of the Poetry command-line interface.
The helper class has the following methods:

``noxfile.Poetry.build(self, *args)``
   Build the package.

``noxfile.Poetry.export(self, *args)``
   Export the lock file to requirements format.

``noxfile.Poetry.version(self)``
   Return the package version.

``noxfile.Poetry.__init__(self, session)``
   Instances need a session object for running commands.


Testing
~~~~~~~

Tests are written using the pytest_ testing framework,
the *de facto* standard for testing in Python.


The test suite
--------------

The test suite is located in the ``tests`` directory::

   tests
   ├── __init__.py
   └── test_main.py

The test suite is `declared as a package <tests-outside-application-code_>`__,
and mirrors the source layout of the package under test.
The file ``test_main.py`` contains tests for the ``__main__`` module.

Initially, the test suite contains a single test case,
checking whether the program exits with a status code of zero.
It also provides a `test fixture`_ using `click.testing.CliRunner`_,
a helper class for invoking the program from within tests.

.. _`tests-outside-application-code`: http://doc.pytest.org/en/latest/goodpractices.html#tests-outside-application-code
.. _`test fixture`: https://docs.pytest.org/en/latest/fixture.html
.. _`click.testing.CliRunner`: https://click.palletsprojects.com/en/7.x/testing/


.. _`The tests session`:

The tests session
-----------------

Run the test suite using the Nox session ``tests``:

.. code:: console

   $ nox --session=tests

The tests session runs the test suite against the installed code.
More specifically, the session builds a wheel from your project and
installs it into the Nox environment,
with dependencies pinned as specified in Poetry's lock file.

You can also run the test suite with a specific Python version.
For example, the following command runs the test suite
using the current stable release of Python:

.. code:: console

   $ nox --session=tests-3.8

Use the separator ``--`` to pass additional options to ``pytest``.
For example, the following command runs only the test case ``test_main_succeeds``:

.. code:: console

   $ nox --session=tests -- -k test_main_succeeds


Test coverage
-------------

*Test coverage* is a measure of the degree to which
the source code of your program is executed while running its test suite.
This project template requires full test coverage.

Code coverage is measured using `Coverage.py`_.
When the test suite completes,
a detailed coverage report is printed to the terminal.
If the total coverage is below 100%,
the test session fails.

Coverage.py is configured using the ``pyproject.toml`` configuration file,
in the ``tool.coverage`` table.
The configuration informs the tool about your package name and source tree layout.
It also enables branch analysis and the display of line numbers for missing coverage,
and specifies the target coverage percentage.


Linting with Flake8
~~~~~~~~~~~~~~~~~~~

This project template comes with an extensive suite of linters,
using the Flake8_ linter framework.
Linters analyze source code to flag
programming errors, bugs, stylistic errors, and suspicious constructs.

By default, the linter suite checks Python files in the following locations:

- ``src``
- ``tests``
- ``noxfile.py``
- ``docs/conf.py``

The configuration file for Flake8 and its extensions
is named ``.flake8`` and located in the project directory.


.. _`The lint session`:

The lint session
----------------

Run the linter suite using the ``lint`` session:

.. code:: console

   $ nox --session=lint

You can also run the linter suite with a specific Python version.
For example, the following command runs the linter suite
using the current stable release of Python:

.. code:: console

   $ nox --session=lint-3.8

Use the separator ``--`` to pass additional options to ``flake8``.
For example, the following command only lints the ``__main__`` module:

.. code:: console

   $ nox --session=lint -- src/<project>/__main__.py


.. _`Available linters`:

Available linters
-----------------

Flake8_ glues together several tools,
and comes with a rich ecosystem of extensions.
The following table lists the linters used by
the *Hypermodern Python Cookiecutter*,
and links to their lists of error codes.

======================= ============================================================== =========
Tool                    Description                                                    Code     
======================= ============================================================== =========
pyflakes_               Find invalid Python code                                       `F <pyflakes codes_>`__
pycodestyle_            Enforce style conventions from `PEP 8`_                        `E,W <pycodestyle codes_>`__
pep8-naming_            Enforce naming conventions from `PEP 8`_                       `N <pep8-naming codes_>`__
flake8-import-order_    Enforce import conventions from `PEP 8`_                       `I <flake8-import-order codes_>`__
flake8-docstrings_      Enforce docstring conventions from `PEP 257`_, via pydocstyle_ `D <pydocstyle codes_>`__
flake8-rst-docstrings_  Find invalid reStructuredText_ in docstrings                   `RST <flake8-rst-docstrings codes_>`__
flake8-black_           Enforce the Black_ code style                                  `BLK <flake8-black codes_>`__
flake8-bugbear_         Detect bugs and design problems                                `B <flake8-bugbear codes_>`__
mccabe_                 Limit the code complexity                                      `C <mccabe codes_>`__
darglint_               Detect inaccurate docstrings                                   `DAR <darglint codes_>`__
flake8-bandit_          Detect common security issues, via Bandit_                     `S <Bandit codes_>`__
======================= ============================================================== =========

The linters
-----------

This section describes the linters in more detail.
Each section also notes any configuration settings applied by
the *Hypermodern Python Cookiecutter*.


pyflakes
........

The pyflakes_ tool
parses Python source files and finds invalid code.
`Error codes`__ are prefixed by ``F`` for "flake".
Warnings reported by this tool include
syntax errors,
undefined names,
unused imports or variables,
and more.
The tool is included with Flake8_ by default.

.. _`pyflakes codes`:
__ https://flake8.pycqa.org/en/latest/user/error-codes.html


pycodestyle
...........

The pycodestyle_ tool
checks your code against many recommendations from `PEP 8`_,
the official Python style guide.
`Error codes`__ are prefixed by ``W`` for warnings and ``E`` for errors.
The tool detects
whitespace and indentation issues,
deprecated features,
bare excepts,
and much more.
The tool is included with Flake8_ by default.

.. _`pycodestyle codes`:
__ https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes

The *Hypermodern Python Cookiecutter* disables the following errors and warnings
for compatibility with Black_ and flake8-bugbear_:

- ``E203`` (whitespace before ``:``)
- ``E501`` (line too long)
- ``W503`` (line break before binary operator)


pep8-naming
...........

The pep8-naming_ tool enforces the naming conventions from `PEP 8`_.
`Error codes`__ are prefixed by ``N`` for "naming".
Examples are the use of camel case for the names of classes,
the use of lowercase for the names of functions, arguments and variables,
or the convention to name the first argument of methods ``self``.

.. _`pep8-naming codes`:
__ https://github.com/pycqa/pep8-naming#pep-8-naming-conventions


flake8-import-order
...................

The flake8-import-order_ plugin
checks that import order adheres to `PEP 8`_
and a configurable style convention.
`Error codes`__ are prefixed by ``I`` for "import".

.. _`flake8-import-order codes`:
__ https://github.com/PyCQA/flake8-import-order#warnings

The *Hypermodern Python Cookiecutter* 
selects the recommendations of the
`Google styleguide <Google import style_>`__.
Imports need to be arranged in three sorted groups, like this:

.. _`Google import style`: https://google.github.io/styleguide/pyguide.html?showone=Imports_formatting#313-imports-formatting

.. code:: python

   # standard library
   import time

   # third-party packages
   import click

   # local packages
   import <package>

The configuration also ensures that
the package name is recognized as local.


pydocstyle and flake8-docstrings
................................

The pydocstyle_ tool is used to check that
docstrings comply with the recommendations of `PEP 257`_
and a configurable style convention.
It is integrated via the flake8-docstrings_ extension.
`Error codes`__ are prefixed by ``D`` for "docstring".
Warnings range from missing docstrings to
issues with whitespace, quoting, and docstring content.

.. _`pydocstyle codes`:
__ http://www.pydocstyle.org/en/stable/error_codes.html

The *Hypermodern Python Cookiecutter*
selects the recommendations of the
`Google styleguide <Google docstring style_>`__.
Here is an example of a function documented in Google style:

.. code:: python

   def add(first: int, second: int) -> int:
       """Add two integers.

       Args:
           first: The first argument.
           second: The second argument.

       Returns:
           The sum of the arguments.
       """

.. _`Google docstring style`: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings.


flake8-rst-docstrings
.....................

The flake8-rst-docstrings_ plugin
validates docstring markup as reStructuredText_ (reST).
Docstrings must be valid reST---which includes most plain text---because
they are used to generate API documentation.
`Error codes`__ are prefixed by ``RST`` for "reStructuredText",
and group issues into numerical blocks, by their severity and origin.

.. _`flake8-rst-docstrings codes`:
__ https://github.com/peterjc/flake8-rst-docstrings#flake8-validation-codes


flake8-black
............

The flake8-black_ plugin
checks adherence to the Black_ code style.
`Error codes`__ are prefixed by ``BLK`` for "black".
It generates a warning if it detects that Black would reformat a source file.
You can fix these issues automatically,
as described below in the section `Code formatting with Black`_.

.. _`flake8-black codes`:
__ https://github.com/peterjc/flake8-black#flake8-validation-codes


flake8-bugbear
..............

flake8-bugbear_ detects bugs and design problems.
`Error codes`__ are prefixed by ``B`` for "bugbear".
The warnings are more opinionated than those of pyflakes or pycodestyle.
For example,
the plugin detects Python 2 constructs which have been removed in Python 3,
and likely bugs such as function arguments defaulting to empty lists or dictionaries.

The *Hypermodern Python Cookiecutter*
also enables Bugbear's ``B9`` warnings,
which are disabled by default.
In particular, ``B950`` checks the maximum line length
like pycodestyle_'s ``E501``,
but with a tolerance margin of 10%.
This soft limit is set to 80 characters,
which is the value used by the Black code formatter.

.. _`flake8-bugbear codes`:
__ https://github.com/PyCQA/flake8-bugbear#list-of-warnings


mccabe
......

The mccabe_ tool
checks the `code complexity <Cyclomatic complexity_>`__
of your Python package against a configured limit.
`Error codes`__ are prefixed by ``C`` for "complexity".
It is included with Flake8_.

.. _`mccabe codes`:
__ https://github.com/PyCQA/mccabe#plugin-for-flake8

The *Hypermodern Python Cookiecutter*
limits code complexity to a value of 10.

.. _`Cyclomatic complexity`: https://en.wikipedia.org/wiki/Cyclomatic_complexity


darglint
........

The darglint_ tool checks that docstring descriptions match function definitions.
`Error codes`__ are prefixed by ``DAR`` for "darglint".
The tool has its own configuration file, named ``.darglint``.

The *Hypermodern Python Cookiecutter*
allows one-line docstrings without function signatures.
Multi-line docstrings must
specify the function signatures completely and correctly,
using `Google docstring style`_.

.. _`darglint codes`:
__ https://github.com/terrencepreilly/darglint#error-codes


Bandit
......

Bandit_ is a tool designed to
find common security issues in Python code,
and integrated via the flake8-bandit_ extension.
`Error codes`__ are prefixed by ``S`` for "security".
(The prefix ``B`` for "bandit" is used
when Bandit is run as a stand-alone tool.)

The *Hypermodern Python Cookiecutter*
disables ``S101`` (use of assert) for the test suite,
as pytest_ uses assertions to verify expectations in tests.

.. _`Bandit codes`:
__ https://bandit.readthedocs.io/en/latest/plugins/index.html#complete-test-plugin-listing


.. _`Code formatting with Black`:

Code formatting with Black
~~~~~~~~~~~~~~~~~~~~~~~~~~

Black_ is the uncompromising Python code formatter.
One of its greatest features is its lack of configurability.
Blackened code looks the same regardless of the project you're reading.

The *Hypermodern Python Cookiecutter*
adheres to Black code style.


.. _`The black session`:

The black session
-----------------

Run the code formatter using the ``black`` session:

.. code:: console

   $ nox --session=black

This session always runs with the current version of Python.

Use the separator ``--`` to pass additional options to ``black``.
For example, the following command formats a specific file:

.. code:: console

   $ nox --session=black -- noxfile.py

By default, the code formatter runs on Python files in the following locations:

- ``src``
- ``tests``
- ``noxfile.py``
- ``docs/conf.py``


Scanning dependencies with Safety
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Safety_ checks the dependencies of your project for known security vulnerabilities,
using a curated database of insecure Python packages.
The *Hypermodern Python Cookiecutter* uses the `poetry export`_ command
to convert Poetry's lock file to a `requirements file`_,
for consumption by Safety.

.. _`poetry export`: https://python-poetry.org/docs/cli/#export
.. _`requirements file`: https://pip.readthedocs.io/en/stable/user_guide/#requirements-files


.. _`The safety session`:

The safety session
------------------

Run Safety_ using the ``safety`` session:

.. code:: console

   $ nox --session=safety

This session always runs with the current version of Python.


.. _`Linting with pre-commit`:

Linting with pre-commit
~~~~~~~~~~~~~~~~~~~~~~~

pre-commit_ is a multi-language linter framework and a Git hook manager.
It allows you to
integrate the best industry standard linters into your Git workflow,
even when written in a language other than Python.
Linters run in isolated environments managed by pre-commit.

When installed as a *pre-commit* `Git hook`_,
pre-commit runs automatically every time you invoke ``git commit``.
The commit is aborted if any check fails.
This workflow allows you to review the changes
before attempting the commit again.
Many linters support fixing offending lines automatically.

.. _`Git hook`: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks


Installation and configuration
------------------------------

Install pre-commit via pipx_:

.. code:: console

   $ pipx install pre-commit

pre-commit is configured using the file ``.pre-commit-config.yaml``
in the project directory.
Please refer to the `official documentation`__
for details about the configuration file.


Available hooks
---------------

The *Hypermodern Python Cookiecutter* comes with
a pre-commit configuration
consisting of the following hooks:

__ https://pre-commit.com/#adding-pre-commit-plugins-to-your-project

======================== ===============================================
Hook                     Description
======================== ===============================================
`black <Black_>`__       Run the Black_ code formatter
`flake8 <Flake8_>`__     Run the Flake8_ linter
`mypy <mypy_>`__         Run the mypy_ static type checker
`prettier <Prettier_>`__ Run the Prettier_ code formatter
check-yaml_              Validate YAML_ files
end-of-file-fixer_       Ensure files are terminated by a single newline
trailing-whitespace_     Ensure lines do not contain trailing whitespace
======================== ===============================================

.. _`check-yaml`: https://github.com/pre-commit/pre-commit-hooks#check-yaml
.. _`end-of-file-fixer`: https://github.com/pre-commit/pre-commit-hooks#end-of-file-fixer
.. _`trailing-whitespace`: https://github.com/pre-commit/pre-commit-hooks#trailing-whitespace

Black_, Flake8_, and mypy_ are run via Poetry using a `repository-local hook`_.
This allows you to manage these tools as development dependencies in Poetry,
rather than having duplicate and potentially diverging version pins in the pre-commit configuration.
This does require you, however, to run `poetry install`_
before you can use pre-commit with your project.

.. _`repository-local hook`: https://pre-commit.com/#repository-local-hooks

These checks run somewhat faster than the corresponding Nox sessions,
for several reasons:

- They only run on files staged for a commit, by default.
- They only run in the active Poetry environment.
- They assume that the tools are already installed.


Command-line usage
------------------

Install the *pre-commit* Git hook by running the following command:

.. code:: console

   $ pre-commit install

The default behaviour of pre-commit is to run on the staged contents of files,
which is useful when it is triggered from a *pre-commit* Git hook:

.. code:: console

   $ pre-commit run

You can run pre-commit on all files instead using the following command:

.. code:: console

   $ pre-commit run --all-files

You can also run a specific pre-commit hook, such as the code formatter Prettier_:

.. code:: console

   $ pre-commit run --all-files prettier


Type-checking
~~~~~~~~~~~~~

`Type annotations`_, first introduced in Python 3.5,
are a way to annotate functions and variables with types.
With appropriate tooling,
they can make your programs easier to understand, debug, and maintain.
There is also an increasing number of libraries
that leverage type annotations at runtime.
For example, you can use type annotations to generate serialization schemas
or command-line parsers.

.. _`Type annotations`: https://docs.python.org/3/library/typing.html

*Type-checking* refers to the practice of
verifying the type correctness of a program,
using type annotations and type inference.
There are two kinds of type checkers:

- *Static type checkers* verify the type correctness of your program
  without executing it, using static analysis.
- *Runtime type checkers* find type errors by instrumenting your code to
  type-check arguments and return values in function calls.
  This is particularly useful during the execution of unit tests.

The *Hypermodern Python Cookiecutter* uses
both a static type checker and a runtime type checker:

- mypy_ is the pioneer and *de facto* reference implementation of
  static type checking in Python.
- Typeguard_ is a runtime type checker and pytest_ plugin.
  It can type-check function calls during test runs via an `import hook`__.

__ https://docs.python.org/3/reference/import.html#import-hooks


.. _`The mypy session`:

The mypy session
----------------

Run mypy_ using Nox:

.. code:: console

   $ nox --session=mypy

You can also run the type checker with a specific Python version.
For example, the following command runs mypy
using the current stable release of Python:

.. code:: console

   $ nox --session=mypy-3.8

Use the separator ``--`` to pass additional options and arguments to ``mypy``.
For example, the following command type-checks only the ``__main__`` module:

.. code:: console

   $ nox --session=mypy -- src/<package>/__main__.py


Configuring mypy
----------------

Configure mypy using the `mypy.ini`__ configuration file.

__ https://mypy.readthedocs.io/en/stable/config_file.html

The *Hypermodern Python Cookiecutter* enables the strictness options
(the options enabled by the :option:`--strict <mypy --strict>` flag):

- :option:`check_untyped_defs <mypy --check-untyped-defs>`
- :option:`disallow_any_generics <mypy --disallow-any-generics>`
- :option:`disallow_incomplete_defs <mypy --disallow-incomplete-defs>`
- :option:`disallow_subclassing_any <mypy --disallow-subclassing-any>`
- :option:`disallow_untyped_calls <mypy --disallow-untyped-calls>`
- :option:`disallow_untyped_decorators <mypy --disallow-untyped-decorators>`
- :option:`disallow_untyped_defs <mypy --disallow-untyped-defs>`
- :option:`no_implicit_optional <mypy --no-implicit-optional>`
- :option:`no_implicit_reexport <mypy --no-implicit-reexport>`
- :option:`strict_equality <mypy --strict-equality>`
- :option:`warn_redundant_casts <mypy --warn-redundant-casts>`
- :option:`warn_return_any <mypy --warn-return-any>`
- :option:`warn_unused_configs <mypy --warn-unused-configs>`
- :option:`warn_unused_ignores <mypy --warn-unused-ignores>`

The :option:`ignore_missing_imports <mypy --ignore-missing-imports>` option
is used to disable import errors for selected packages
where type information is not yet available.

The following options are enabled for enhanced output:

- :option:`pretty <mypy --pretty>`
- :option:`show_column_numbers <mypy --show-column-numbers>`
- :option:`show_error_codes <mypy --show-error-codes>`
- :option:`show_error_context <mypy --show-error-context>`


.. _`The typeguard session`:

The typeguard session
---------------------

Run Typeguard_ using Nox:

.. code:: console

   $ nox --session=typeguard

The typeguard session runs the test suite with runtime type-checking enabled.
It is similar to the `tests session <The tests session_>`__,
with the difference that your package is instrumented by Typeguard.

Typeguard_ checks that arguments passed to functions
match the type annotations of the function parameters,
and that the return value provided by the function
matches the return type annotation.
In the case of generator functions,
Typeguard checks the yields, sends and the return value
against the ``Generator`` or ``AsyncGenerator`` annotation.

You can run the session with a specific Python version.
For example, the following command runs the session
with the current stable release of Python:

.. code:: console

   $ nox --session=typeguard-3.8

Use the separator ``--`` to pass additional options and arguments to pytest.
For example, the following command runs only tests for the ``__main__`` module:

.. code:: console

   $ nox --session=typeguard -- tests/test_main.py

Typeguard generates a warning about missing type annotations for a Click object.
This is due to the fact that ``__main__.main`` is wrapped by a decorator,
and its type annotations only apply to the inner function,
not the resulting object as seen by the test suite.


Documentation
~~~~~~~~~~~~~

Stand-alone documents
---------------------

The project repository contains several documentation files
written in reStructuredText_:

======================= ============================================
File                    Contents
======================= ============================================
``README.rst``          Project description for GitHub and PyPI
``CONTRIBUTING.rst``    Contributor Guide
``CODE_OF_CONDUCT.rst`` Code of Conduct
``LICENSE.rst``         License
======================= ============================================


Sphinx documentation
--------------------

The project documentation itself lives under ``docs``.
It is written in reStructuredText_,
processed by Sphinx_,
and accessible on `Read the Docs`_.
It consists of the following files:

====================== =======================================================
File                   Contents
====================== =======================================================
``conf.py``            Sphinx configuration file
``index.rst``          Master document
``contributing.rst``   Contributor Guide (includes ``CONTRIBUTING.rst``)
``codeofconduct.rst``  Code of Conduct (includes ``CODE_OF_CONDUCT.rst``)
``license.rst``        License (includes ``LICENSE.rst``)
``reference.rst``      API documentation
``requirements.txt``   Build dependencies for `Read the Docs`_
====================== =======================================================

The documentation menu also has a *Changelog* entry,
which links to the `GitHub Releases <GitHub Release_>`__ page.

The API documentation is generated from docstrings and type annotations
using the autodoc_ and napoleon_ extensions.

The ``requirements.txt`` is necessary
because Read the Docs currently does not support
installing development dependencies using Poetry's lock file.
You need to update this file manually,
whenever you upgrade Sphinx or its extensions.
For the sake of brevity and maintainability,
only direct dependencies are listed.


.. _`The docs session`:

The docs session
-----------------

Build the documentation using the Nox session ``docs``:

.. code:: console

   $ nox --session=docs

The docs session runs the command ``sphinx-build``
to generate the HTML documentation from the Sphinx directory.

In `interactive mode`__---such
as when invoking Nox from a terminal---sphinx-autobuild_ is used instead.
This tool has several advantages
when you are editing the documentation files:

__ https://nox.thea.codes/en/stable/usage.html#forcing-non-interactive-behavior

- It rebuilds the documentation whenever a change is detected.
- It spins up a web server with live reloading.
- It opens the location of the web server in your browser.

.. _`sphinx-autobuild`: https://github.com/GaretJax/sphinx-autobuild

Use the ``--`` separator to pass additional options to either tool.
For example, to treat warnings as errors and run in nit-picky mode:

.. code:: console

   $ nox --session=docs -- -W -n docs docs/_build

This Nox session always runs with the current major release of Python.


.. _`The xdoctest session`:

The xdoctest session
--------------------

The xdoctest_ tool
runs examples in your docstrings and
compares the actual output to the expected output as per the docstring.
This serves multiple purposes:

- The example is checked for correctness.
- You ensure that the documentation is up-to-date.
- Your codebase gets additional test coverage for free.

Run the tool using the Nox session ``xdoctest``:

.. code:: console

   $ nox --session=xdoctest

You can also run the test suite with a specific Python version.
For example, the following command runs the examples
using the current stable release of Python:

.. code:: console

   $ nox --session=xdoctest-3.8

By default, the Nox session uses the ``all`` subcommand to run all examples.
You can also list examples using the ``list`` subcommand,
or run specific examples:

.. code:: console

   $ nox --session=xdoctest -- list


Continuous integration using GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The *Hypermodern Python Cookiecutter* uses `GitHub Actions`_
to implement continuous integration and delivery.
With GitHub Actions,
you define so-called workflows
using `YAML`_ files located in the ``.github/workflows`` directory.

A *workflow* is an automated process
consisting of one or many jobs,
each of which executes a series of steps.
Workflows are triggered by events,
for example when a commit is pushed
or when a release is published.
You can learn more about
the workflow language and its supported keywords
in the `official reference`__.

__ https://help.github.com/en/actions/automating-your-workflow-with-github-actions/workflow-syntax-for-github-actions

Real-time logs for workflow runs are available
from the *Actions* tab in your GitHub repository.


External Services
-----------------

Your repository can be integrated with several external services
for continuous integration and delivery.
This section describes these external services,
what they do, and how to set them up for your repository.


PyPI
....

PyPI_ is the official Python Package Index.
Uploading your package to PyPI allows others to
download and install it to their system.

Follow these steps to set up PyPI for your repository:

1. Sign up at PyPI_.
2. Go to the Account Settings on PyPI,
   generate an API token, and copy it.
3. Go to the repository settings on GitHub, and
   add a secret named ``PYPI_TOKEN`` with the token you just copied.

PyPI is integrated with your repository
via the `Release workflow <The Release workflow_>`__.


TestPyPI
........

TestPyPI_ is a test instance of the Python package registry.
It allows you to check your release before uploading it to the real index.

Follow these steps to set up TestPyPI for your repository:

1. Sign up at TestPyPI_.
2. Go to the Account Settings on TestPyPI,
   generate an API token, and copy it.
3. Go to the repository settings on GitHub, and
   add a secret named ``TEST_PYPI_TOKEN`` with the token you just copied.

TestPyPI is integrated with your repository
via the `TestPyPI workflow <The TestPyPI workflow_>`__.


Codecov
.......

Codecov_ is a reporting service for code coverage.

Follow these steps to set up Codecov for your repository:

1. Sign up at Codecov_.
2. Install their GitHub app.
3. Add your repository to Codecov.

The configuration is included in the repository, as ``codecov.yml``.

Codecov integrates with your repository
via its GitHub app.
The `Coverage workflow <The Coverage workflow_>`__ uploads the coverage data.


Dependabot
..........

Dependabot_ creates pull requests with automated dependency updates.

Follow these steps to set up Dependabot for your repository:

1. Sign up at Dependabot_.
2. Install their GitHub app.
3. Add your repository to Dependabot.

The configuration is included in the repository, as ``.dependabot/config.yml``.

Dependabot integrates with your repository via its GitHub app.


Read the Docs
.............

`Read the Docs`_ automates the building, versioning, and hosting of documentation.

Follow these steps to set up Read the Docs for your repository:

1. Sign up at `Read the Docs`_.
2. Import your GitHub repository, using the button *Import a Project*.

The configuration is included in the repository, as ``.readthedocs.yml``.

Read the Docs integrates with your repository via a webhook__.

__ https://docs.readthedocs.io/en/stable/webhooks.html


Secrets
-------

Some workflows use tokens to access external services.
The following table lists the required tokens,
which need to be stored as secrets in the repository settings on GitHub:

=================== ===================
Name                Description
=================== ===================
``PYPI_TOKEN``      PyPI_ API token
``TEST_PYPI_TOKEN`` TestPyPI_ API token
=================== ===================

You can generate these API tokens
from your account settings on PyPI_ and TestPyPI_.


Constraints file
----------------

GitHub workflows install the following tools:

- pip_
- Poetry_
- Nox_
- pre-commit_

These dependencies are pinned using a `constraints file`__
located in ``.github/workflow/constraints.txt``.

__ https://pip.pypa.io/en/stable/user_guide/#constraints-files

Upgrade to newer versions of these tools by updating the constraints file.

.. note::

   Keep the constraints file up-to-date manually.
   It is not yet managed by Dependabot_.


Available workflows
-------------------

The *Hypermodern Python Cookiecutter* defines
the following workflows:

=================================================== ======================== ==================================== ===============
Workflow                                            File                     Description                          Trigger
=================================================== ======================== ==================================== ===============
`Tests <The Tests workflow_>`__                     ``tests.yml``            Run the test suite with Nox_         Push
`Coverage <The Coverage workflow_>`__               ``coverage.yml``         Upload coverage data to Codecov_     Push
`pre-commit <The pre-commit workflow_>`__           ``pre-commit.yml``       Run linters with pre-commit_         Push
`Build documentation <The Docs workflow_>`__        ``docs.yml``             Build the documentation with Sphinx_ Push
`Release Drafter <The Release Drafter workflow_>`__ ``release-drafter.yml``  Update the draft GitHub Release      Push (master)
`Release <The Release workflow_>`__                 ``release.yml``          Upload the package to PyPI_          GitHub Release
`TestPyPI <The TestPyPI workflow_>`__               ``test-pypi.yml``        Upload the package to TestPyPI_      Push (master)
=================================================== ======================== ==================================== ===============


.. _`The Tests workflow`:

The Tests workflow
..................

The Tests workflow executes the test suite using Nox.

The workflow is triggered on every push to the GitHub repository.
It consists of a job for each supported Python version,
executed on the `latest supported runners`__ for
Ubuntu, Windows, and macOS.

__ https://help.github.com/en/actions/automating-your-workflow-with-github-actions/virtual-environments-for-github-hosted-runners#supported-runners-and-hardware-resources

The workflow uses the following GitHub Actions:

- `actions/checkout`_ for checking out the Git repository
- `actions/setup-python`_ for setting up the Python interpreter

.. _`actions/checkout`: https://github.com/actions/checkout
.. _`actions/setup-python`: https://github.com/actions/setup-python

The workflow is defined in ``.github/workflows/tests.yml``.


.. _`The Coverage workflow`:

The Coverage workflow
.....................

The Coverage workflow uploads coverage data to Codecov_.

The workflow is triggered on every push to the GitHub repository.
It executes the `tests session <the tests session_>`__
to generate a coverage report in `cobertura`__ XML format.
This coverage report is then uploaded to Codecov_.

__ https://cobertura.github.io/cobertura/

The workflow uses the following GitHub Actions:

- `actions/checkout`_ for checking out the Git repository
- `actions/setup-python`_ for setting up the Python interpreter
- `codecov/codecov-action`_ for uploading to Codecov_

.. _`codecov/codecov-action`: https://github.com/codecov/codecov-action

The workflow runs with the current Python version,
using the latest supported Ubuntu runner.

It is defined in ``.github/workflows/coverage.yml``.


.. _`The pre-commit workflow`:

The pre-commit workflow
.......................

The pre-commit workflow runs `pre-commit <Linting with pre-commit_>`__
on all files in the repository.

The workflow is triggered on every push to the GitHub repository.

The workflow uses the following GitHub Actions:

- `actions/checkout`_ for checking out the Git repository
- `actions/setup-python`_ for setting up the Python interpreter
- `actions/cache`_ for caching pre-commit environments

.. _`actions/cache`: https://github.com/actions/cache

The workflow runs with the current Python version,
using the latest Ubuntu, Windows, and macOS runners.

It is defined in ``.github/workflows/pre-commit.yml``.


.. _`The Docs workflow`:

The Docs workflow
.................

The Docs workflow builds the Sphinx_ documentation
using the `docs <The docs session_>`__ Nox session,
and uploads the generated files as a `workflow artifact`__.

__ https://help.github.com/en/actions/configuring-and-managing-workflows/persisting-workflow-data-using-artifacts

This is done solely to ensure that the build process is functional.
The actual project documentation is built independently on `Read the Docs`_.

The workflow is triggered on every push to the GitHub repository.

The workflow uses the following GitHub Actions:

- `actions/checkout`_ for checking out the Git repository
- `actions/setup-python`_ for setting up the Python interpreter
- `actions/upload-artifact`_ to upload the generated documentation

.. _`actions/upload-artifact`: https://github.com/actions/upload-artifact

The workflow runs with the current Python version,
using the latest supported Ubuntu runner.

It is defined in ``.github/workflows/docs.yml``.


.. _`The Release Drafter workflow`:

The Release Drafter workflow
............................

The Release Drafter workflow maintains a draft for the next GitHub Release.

The workflow is triggered on every push to the master branch.
It includes details from every pull request merged into master since the last release.
The workflow uses the `Release Drafter`_ GitHub Action.

The *Hypermodern Python Cookiecutter* groups pull requests by type,
using GitHub labels.
The following table shows the section headings and corresponding labels:

.. include:: ../README.rst
   :start-after: table-release-drafter-sections-begin
   :end-before: table-release-drafter-sections-end

The workflow is defined in ``.github/workflows/release-drafter.yml``.
The configuration file is located in ``.github/release-drafter.yml``.


.. _`The Release workflow`:

The Release workflow
....................

The Release workflow publishes your package on PyPI_, the Python Package Index.

The workflow is triggered when a GitHub Release is published.
It checks that the test suite passes,
builds the package using Poetry,
and uploads it using the `pypa/gh-action-pypi-publish`_ action.
This workflow uses the ``PYPI_TOKEN`` secret.

.. _`pypa/gh-action-pypi-publish`: https://github.com/pypa/gh-action-pypi-publish

The workflow is defined in ``.github/workflows/release.yml``.


.. _`The TestPyPI workflow`:

The TestPyPI workflow
.....................

The TestPyPI workflow publishes your package on TestPyPI_,
a test instance of the Python Package Index.

The workflow is triggered on every push to the master branch.
It bumps the version number to a developmental pre-release,
builds the package using Poetry,
and uploads it using the `pypa/gh-action-pypi-publish`_ action.
This workflow uses the ``TEST_PYPI_TOKEN`` secret.

The workflow is defined in ``.github/workflows/test-pypi.yml``.


Read the Docs
~~~~~~~~~~~~~

`Read the Docs`_ hosts documentation for countless open-source Python projects.
The hosting service also takes care of rebuilding the documentation
when you update your project.
Users can browse documentation
for every published version, as well as the latest development version.

Sign up at Read the Docs,
and import your GitHub repository, using the button *Import a Project*.
Read the Docs automatically starts building your
documentation. When the build has completed, your documentation will have a
public URL like this:

   *https://<project>.readthedocs.io/*

The configuration file is named ``.readthedocs.yml`` in the project directory.
The *Hypermodern Python Cookiecutter* configures Read the Docs
to build and install the package with Poetry,
using a so-called `PEP 517`_-build.

Build dependencies for the documentation
are installed using the file ``docs/requirements.txt``.
Note that this file partially duplicates Poetry's lock file.
It needs to be kept up-to-date manually,
whenever you upgrade Sphinx, and
whenever you add, upgrade, or remove a Sphinx extension.


.. _`Tutorials`:

Tutorials
~~~~~~~~~

First, make sure you have all the `requirements <Installation_>`__ installed.


How to test your project
------------------------

Run the test suite using `Nox <Using Nox_>`__:

.. code:: console

   $ nox -r

Additional checks are provided by `pre-commit <Linting with pre-commit_>`__:

.. code:: console

   $ pre-commit run --all-files


How to run your code
--------------------

First, install the project and its dependencies to the Poetry environment:

.. code:: console

   $ poetry install

Run an interactive session in the environment:

.. code:: console

   $ poetry run python

Invoke the command-line interface of your package:

.. code:: console

   $ poetry run <project>

  
How to make code changes
------------------------

1. | Run the tests, `as explained above <How to test your project_>`__.
   | All tests should pass.
2. | Add a failing test `under the tests directory <Testing_>`__.
   | Run the tests again to verify that your test fails.
3. | Make your changes to the package, `under the src directory <The initial package_>`__.
   | Run the tests to verify that all tests pass again.


How to push code changes
------------------------

Create a branch for your changes:

.. code:: console

   $ git switch --create my-topic-branch master

Create a series of small, single-purpose commits:

.. code:: console

   $ git add <files>
   $ git commit

Push your branch to GitHub:

.. code:: console

   $ git push --set-upstream origin my-topic-branch

The push triggers the following automated steps:

- `The test suite runs against your branch <The Tests workflow_>`__.
- `Coverage data is uploaded to Codecov <The Coverage workflow_>`__.
- `The pre-commit linter suite runs against your branch <The pre-commit workflow_>`__.
- `The documentation is built from your branch <The Docs workflow_>`__.


How to open a pull request
--------------------------

Open a pull request for your branch on GitHub:

1. Select your branch from the *Branch* menu.
2. Click **New pull request**.
3. Enter the title for the pull request.
4. Enter a description for the pull request.
5. Apply a `label identifying the type of change <The Release Drafter workflow_>`_.
6. Click **Create pull request**.

Release notes are pre-filled with the titles of merged pull requests.


How to accept a pull request
----------------------------

If all checks are marked as passed,
merge the pull request using the squash-merge strategy (recommended):

1. Click **Squash and Merge**.
   (Select this option from the dropdown menu of the merge button, if it is not shown.)
2. Click **Confirm squash and merge**.
3. Click **Delete branch**.

This triggers the following automated steps:

- `The test suite runs against the master branch <The Tests workflow_>`__.
- `Coverage data is uploaded to Codecov <The Coverage workflow_>`__.
- `The pre-commit linter suite runs against the master branch <The pre-commit workflow_>`__.
- `The documentation is built from the master branch <The Docs workflow_>`__.
- `The draft GitHub Release is updated <The Release Drafter workflow_>`__.
- `A pre-release of the package is uploaded to TestPyPI <The TestPyPI workflow_>`__.
- `Read the Docs`_ rebuilds the *latest* version of the documentation.

In your local repository,
update the master branch:

.. code:: console

   $ git switch master
   $ git pull origin master

Optionally, remove the merged topic branch
from the local repository as well:

.. code:: console

   $ git remote prune origin
   $ git branch --delete --force my-topic-branch

The original commits remain accessible from the pull request
(*Commits* tab).


How to make a release
---------------------

Before making a release, go through the following checklist:

- The master branch passes all checks.
- The development release on `TestPyPI`_ looks good.
- All pull requests for the release have been merged.

Making a release is a two-step process:

1. Bump the version using `poetry version`_. (Commit and push.)
2. Publish a GitHub Release.

.. _`poetry version`: https://python-poetry.org/docs/cli/#version

When bumping the version, adhere to `Semantic Versioning`_ and `PEP 440`_.
The individual steps for bumping the version are:

.. code:: console

   $ git switch master
   $ poetry version <version>
   $ git commit --message="<project> <version>" pyproject.toml
   $ git push origin master

If you want the Git tag to be annotated or signed,
add the following optional steps:

.. code:: console

   $ git tag --message="<project> <version>" v<version>
   $ git push origin v<version>

To publish the release,
locate the draft release on the *Releases* tab of the GitHub repository,
and follow these steps:

1. Click **Edit** next to the draft release.
2. Enter a tag of the form ``v<version>``, using the new project version.
3. Enter the release title, e.g. ``<version>``.
4. Edit the release description, if required.
5. Click **Publish Release**.

After publishing the release,
the following automated steps are triggered:

- The Git tag is applied to the repository.
- `The package is uploaded to PyPI <The Release workflow_>`__.
- `Read the Docs`_ builds a new stable version of the documentation.

Update your local repository:

.. code:: console

   $ git switch master
   $ git pull origin master v<version>


The Hypermodern Python blog
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The project setup is described in detail in the `Hypermodern Python`_ article series:

- `Chapter 1: Setup`_
- `Chapter 2: Testing`_
- `Chapter 3: Linting`_
- `Chapter 4: Typing`_
- `Chapter 5: Documentation`_
- `Chapter 6: CI/CD`_

.. _`Chapter 1: Setup`: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
.. _`Chapter 2: Testing`: https://medium.com/@cjolowicz/hypermodern-python-2-testing-ae907a920260
.. _`Chapter 3: Linting`: https://medium.com/@cjolowicz/hypermodern-python-3-linting-e2f15708da80
.. _`Chapter 4: Typing`: https://medium.com/@cjolowicz/hypermodern-python-4-typing-31bcf12314ff
.. _`Chapter 5: Documentation`: https://medium.com/@cjolowicz/hypermodern-python-5-documentation-13219991028c
.. _`Chapter 6: CI/CD`: https://medium.com/@cjolowicz/hypermodern-python-6-ci-cd-b233accfa2f6

You can also read the articles on `this blog`__.

__ https://cjolowicz.github.io/posts/hypermodern-python-01-setup/

.. include:: ../README.rst
   :start-after: references-begin
   :end-before: references-end

.. _`Calendar Versioning`: https://calver.org
.. _`GitHub Release`: https://help.github.com/en/github/administering-a-repository/about-releases
.. _`Hypermodern Python Cookiecutter`: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _`Jinja`: https://palletsprojects.com/p/jinja/
.. _`MIT license`: https://opensource.org/licenses/MIT
.. _`PEP 257`: http://www.python.org/dev/peps/pep-0257/
.. _`PEP 440`: https://www.python.org/dev/peps/pep-0440/
.. _`PEP 517`: https://www.python.org/dev/peps/pep-0517/
.. _`PEP 518`: https://www.python.org/dev/peps/pep-0518/
.. _`PEP 561`: https://www.python.org/dev/peps/pep-0561/
.. _`PEP 8`: http://www.python.org/dev/peps/pep-0008/
.. _`TOML`: https://github.com/toml-lang/toml
.. _`YAML`: https://yaml.org/
.. _`bash`: https://www.gnu.org/software/bash/
.. _`curl`: https://curl.haxx.se
.. _`darglint`: https://github.com/terrencepreilly/darglint
.. _`flake8-bandit`: https://github.com/tylerwince/flake8-bandit
.. _`flake8-black`: https://github.com/peterjc/flake8-black
.. _`flake8-bugbear`: https://github.com/PyCQA/flake8-bugbear
.. _`flake8-docstrings`: https://gitlab.com/pycqa/flake8-docstrings
.. _`flake8-import-order`: https://github.com/PyCQA/flake8-import-order
.. _`flake8-rst-docstrings`: https://github.com/peterjc/flake8-rst-docstrings 
.. _`git`: https://www.git-scm.com
.. _`mccabe`: https://github.com/PyCQA/mccabe
.. _`pep8-naming`: https://github.com/pycqa/pep8-naming
.. _`pip`: https://pip.pypa.io/
.. _`pycodestyle`: https://pycodestyle.pycqa.org/en/latest/
.. _`pydocstyle`: http://www.pydocstyle.org/
.. _`pyflakes`: https://github.com/PyCQA/pyflakes
.. _`reStructuredText`: https://docutils.sourceforge.io/rst.html
