"""Sphinx configuration."""
from datetime import datetime


project = "Hypermodern Python Cookiecutter"
author = "Claudio Jolowicz"
copyright = f"{datetime.now().year}, {author}"
extensions = ["recommonmark"]
html_theme_options = {
    "logo": "../../Logo.png",
    "logo_name": True,
    "fixed_sidebar": True,
    "sidebar_width": "250px",
}
