"""Sphinx configuration."""
from datetime import datetime


project = "Hypermodern Python Cookiecutter"
author = "Claudio Jolowicz"
copyright = f"{datetime.now().year}, {author}"
extensions = ["recommonmark"]
html_theme_options = {
    "sidebar_width": "250px",
    "fixed_sidebar": True,
}
