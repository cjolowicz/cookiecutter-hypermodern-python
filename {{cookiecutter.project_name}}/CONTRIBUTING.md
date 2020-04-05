# Contributor Guide

Thank you for your interest in improving this project.
This project is open-source under the [MIT License] and
welcomes contributions in the form of bug reports, feature requests, and pull requests.

Here is a list of important resources for contributors:

- [Source Code]
- [Documentation]
- [Issue Tracker]
- [Code of Conduct]

[mit license]: https://opensource.org/licenses/MIT
[source code]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}
[documentation]: https://{{cookiecutter.project_name}}.readthedocs.io/
[issue tracker]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/issues
[code of conduct]: CODE_OF_CONDUCT.md

## How to report a bug

Report bugs on the [Issue Tracker].

When filing an issue, make sure to answer these questions:

- Which operating system and Python version are you using?
- Which version of this project are you using?
- What did you do?
- What did you expect to see?
- What did you see instead?

The best way to get your bug fixed is to provide a test case,
and/or steps to reproduce the issue.

## How to request a feature

Request features on the [Issue Tracker].

## How to set up your development environment

You need Python 3.6+ and the following tools:

- [Poetry]
- [Nox]

Install the package with development requirements:

```console
$ poetry install
```

You can now run an interactive Python session,
or the command-line interface:

```console
$ poetry run python
$ poetry run {{cookiecutter.project_name}}
```

[poetry]: https://python-poetry.org/
[nox]: https://nox.thea.codes/

## How to test the project

Run the full test suite:

```console
$ nox
```

List the available Nox sessions:

```console
$ nox --list-sessions
```

You can also run a specific Nox session.
For example, invoke the unit test suite like this:

```console
$ nox --session=tests
```

Unit tests are located in the `tests` directory,
and are written using the [pytest] testing framework.

[pytest]: https://pytest.readthedocs.io/

## How to submit changes

Open a [pull request] to submit changes to this project.

Your pull request needs to meet the following guidelines for acceptance:

- The Nox test suite must pass without errors and warnings.
- Include unit tests. This project maintains 100% code coverage.
- If your changes add functionality, update the documentation accordingly.

Feel free to submit early, though—we can always iterate on this.

You can ensure that your changes adhere to the code style by reformatting with [Black]:

```console
$ nox --session=black
```

It is recommended to open an issue before starting work on anything.
This will allow a chance to talk it over with the owners and validate your approach.

[pull request]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/pulls
[black]: https://black.readthedocs.io/
