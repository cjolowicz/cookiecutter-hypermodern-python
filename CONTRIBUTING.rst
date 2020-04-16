Contributor Guide
=================

Thank you for your interest in improving the Hypermodern Python Cookiecutter.
This project is open-source under the `MIT license`_ and
welcomes contributions in the form of bug reports, feature requests, and pull requests.

Here is a list of important resources for contributors:

- `Source Code`_
- `Documentation`_
- `Issue Tracker`_
- `Code of Conduct`_

.. _`MIT license`: https://opensource.org/licenses/MIT
.. _`Source Code`: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _`Documentation`: https://cookiecutter-hypermodern-python.readthedocs.io/
.. _`Issue Tracker`: https://github.com/cjolowicz/cookiecutter-hypermodern-python/issues
.. _`Code of Conduct`: https://cookiecutter-hypermodern-python.readthedocs.io/codeofconduct.html


How to report a bug
-------------------

Report bugs on the `Issue Tracker`_.

When filing an issue, make sure to answer these questions:

- Which operating system and Python version are you using?
- Which version of this project are you using?
- What did you do?
- What did you expect to see?
- What did you see instead?

The best way to get your bug fixed is to provide a test case,
and/or steps to reproduce the issue.


How to request a feature
------------------------

Request features on the `Issue Tracker`_.


How to set up your development environment
------------------------------------------

You need Python 3.6+ and the following tools:

- Cookiecutter_
- Poetry_
- Nox_

Fork the repository on GitHub_,
and clone the fork to your local machine. You can now generate a project
from your development version:

.. code:: console

   $ cookiecutter path/to/cookiecutter-hypermodern-python

You may also want to push your generated project to GitHub,
and set up `continuous integration`_.

.. _`Cookiecutter`: https://cookiecutter.readthedocs.io/
.. _`Poetry`: https://python-poetry.org/
.. _`Nox`: https://nox.thea.codes/
.. _`Github`: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _`continuous integration`: https://github.com/cjolowicz/cookiecutter-hypermodern-python/#continuous-integration


How to test the project
-----------------------

Please refer to the `User Guide`_
for instructions on how to run the test suite locally.

.. _`User Guide`: https://cookiecutter-hypermodern-python.readthedocs.io/en/latest/guide.html#how-to-test-your-project


How to submit changes
---------------------

Open a `pull request`_ to submit changes to this project.

Your pull request needs to meet the following guidelines for acceptance:

- The Nox test suite must pass without errors and warnings.
- Include unit tests. This project maintains 100% code coverage.
- If your changes add functionality, update the documentation accordingly.

Feel free to submit early, though—we can always iterate on this.

You can ensure that your changes adhere to the code style by reformatting with Black_:

.. code:: console

   $ nox --session=black

It is recommended to open an issue before starting work on anything.
This will allow a chance to talk it over with the owners and validate your approach.

.. _`pull request`: https://github.com/cjolowicz/cookiecutter-hypermodern-python/pulls
.. _`Black`: https://black.readthedocs.io/


How to accept changes
---------------------

*You need to be a project maintainer to accept changes.*

Before accepting a pull request, go through the following checklist:

-  The PR must pass all checks.
-  The PR must have a descriptive title.
-  The PR should be labelled with the kind of change (see below).

Release notes are pre-filled with titles and authors of merged pull requests.
Labels group the pull requests into sections.
The following list shows the available sections,
with associated labels in parentheses:

-  💥 Breaking Changes (``breaking``)
-  🚀 Features (``enhancement``)
-  🔥 Removals and Deprecations (``removal``)
-  🐞 Fixes (``bug``)
-  🐎 Performance (``performance``)
-  🚨 Testing (``testing``)
-  👷 Continuous Integration (``ci``)
-  📚 Documentation (``documentation``)
-  🔨 Refactoring (``refactoring``)
-  💄 Style (``style``)
-  📦 Dependencies (``dependencies``)

To merge the pull request, follow these steps:

1. Click **Squash and Merge**.
   (Select this option from the dropdown menu of the merge button, if it is not shown.)
2. Click **Confirm squash and merge**.
3. Click **Delete branch**.


How to make a release
---------------------

*You need to be a project maintainer to make a release.*

Before making a release, go through the following checklist:

-  All pull requests for the release have been merged.
-  The master branch passes all checks.

Releases are made by publishing a GitHub Release.
A draft release is being maintained based on merged pull requests.
To publish the release, follow these steps:

1. Click **Edit** next to the draft release.
2. Enter a tag with the new version.
3. Enter the release title, also the new version.
4. Edit the release description, if required.
5. Click **Publish Release**.

Version numbers adhere to `Calendar Versioning`_,
of the form ``YYYY.MM.DD``.

After publishing the release, the following automated steps are triggered:

- The Git tag is applied to the repository.
- `Read the Docs`_ builds a new stable version of the documentation.

.. _`Calendar Versioning`: https://calver.org/
.. _`Read the Docs`: https://cookiecutter-hypermodern-python.readthedocs.io/
