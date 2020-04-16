"""Sphinx configuration."""
from datetime import datetime


project = "{{cookiecutter.friendly_name}}"
author = "{{cookiecutter.author}}"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx_autodoc_typehints"]
