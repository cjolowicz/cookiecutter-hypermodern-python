"""Sphinx configuration."""
from datetime import datetime


project = "Hypermodern Python Cookiecutter"
author = "Claudio Jolowicz"
copyright = f"{datetime.now().year}, {author}"
extensions = ["recommonmark"]
html_theme_options = {
    "github_banner": "true",
    "github_button": "true",
    "github_count": "true",
    "github_user": "cjolowicz",
    "github_repo": "cookiecutter-hypermodern-python",
    "github_type": "star",
    "logo": "../../Logo.png",
    "logo_name": True,
    "fixed_sidebar": True,
    "sidebar_width": "250px",
}
