{%- macro heading(text) -%}
{{text}}
{% for _ in text %}={% endfor %}
{%- endmacro -%}
{{ heading(cookiecutter.friendly_name) }}

|PyPI| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg
   :target: https://pypi.org/project/{{cookiecutter.project_name}}/
   :alt: PyPI
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}}
   :target: https://pypi.org/project/{{cookiecutter.project_name}}
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/{{cookiecutter.project_name}}
   :target: https://opensource.org/licenses/{{cookiecutter.license}}
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/{{cookiecutter.project_name}}/latest.svg?label=Read%20the%20Docs
   :target: https://{{cookiecutter.project_name}}.readthedocs.io/
   :alt: Read the documentation at https://{{cookiecutter.project_name}}.readthedocs.io/
.. |Tests| image:: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/workflows/Tests/badge.svg
   :target: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


Features
--------

* TODO


Requirements
------------

* TODO


Installation
------------

You can install *{{cookiecutter.friendly_name}}* via pip_ from PyPI_:

.. code:: console

   $ pip install {{cookiecutter.project_name}}


Usage
-----

Please see the `Command-line Reference <Usage_>`_ for details.


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the `{{cookiecutter.license.replace("-", " ")}} license`_,
*{{cookiecutter.friendly_name}}* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

This project was generated from `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.

.. _@cjolowicz: https://github.com/cjolowicz
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _{{cookiecutter.license.replace("-", " ")}} license: https://opensource.org/licenses/{{cookiecutter.license}}
.. _PyPI: https://pypi.org/
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _file an issue: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
.. _Usage: https://{{cookiecutter.project_name}}.readthedocs.io/en/latest/usage.html
