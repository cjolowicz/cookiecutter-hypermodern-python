Hypermodern Python Cookiecutter
===============================

.. toctree::
   :hidden:
   :maxdepth: 1

   Quickstart <quickstart>
   guide
   CONTRIBUTING
   Code of Conduct <CODE_OF_CONDUCT>
   license
   Changelog <https://github.com/cjolowicz/cookiecutter-hypermodern-python/releases>

|Tests| |CalVer|

.. |Tests| image:: https://github.com/cjolowicz/cookiecutter-hypermodern-python/workflows/Tests/badge.svg
   :target: https://github.com/cjolowicz/cookiecutter-hypermodern-python/actions?workflow=Tests
.. |CalVer| image:: https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg
   :target: http://calver.org/

Cookiecutter_ template for a Python package
based on the `Hypermodern Python`_ article series.


Usage
-----

.. code:: console

   $ cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python \
     --checkout="2020.4.15.1"


Features
--------

.. include:: guide.rst
   :start-after: features-begin
   :end-before: features-end


FAQ
---

  *What is this project about?*

The mission of this project is to
enable current best practises
through modern Python tooling.

  *What makes this project different from other Python templates?*

This is a general-purpose template for Python libraries and applications.

Our goals are:

- Keep a focus on simplicity and minimalism
- Promote code quality through automation
- Provide reliable and repeatable processes

The project template is centered around the following tools:

- Poetry_ for packaging and dependency management
- Nox_ for automation of checks and other development tasks
- `GitHub Actions`_ for continuous integration and delivery

  *Why is this Python template called "hypermodern"?*

Hypermodernism_ is a school of chess from a century ago.
If this setup ever goes out of fashion,
I can pretend it was my secret plan from the start.
All images on the
`associated blog <Hypermodern Python_>`__ show
`outdated visions <Retrofuturism_>`__ of the future.

.. _`Hypermodernism`: https://en.wikipedia.org/wiki/Hypermodernism_(chess)
.. _`Retrofuturism`: https://en.wikipedia.org/wiki/Retrofuturism

.. include:: guide.rst
   :start-after: references-begin
   :end-before: references-end
