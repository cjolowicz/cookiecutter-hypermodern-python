"""Nox sessions."""
from pathlib import Path
import shutil

import nox
from nox.sessions import Session


@nox.session
def docs(session: Session) -> None:
    """Build the documentation."""
    builddir = Path("docs", "_build")
    if builddir.exists():
        shutil.rmtree(builddir)
    session.install("sphinx", "recommonmark")
    session.run("sphinx-build", "docs", "docs/_build")
