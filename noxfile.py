"""Nox sessions."""
from pathlib import Path
import shutil

import nox
import nox_poetry.patch
from nox.sessions import Session


@nox.session
def docs(session: Session) -> None:
    """Build the documentation."""
    args = session.posargs or ["-W", "-n", "docs", "docs/_build"]

    if session.interactive and not session.posargs:
        args = ["-a", "--watch=docs/_static", "--open-browser", *args]

    builddir = Path("docs", "_build")
    if builddir.exists():
        shutil.rmtree(builddir)

    if session.interactive:
        session.install("sphinx-autobuild")
        session.run("sphinx-autobuild", *args)
    else:
        session.install("sphinx")
        session.run("sphinx-build", *args)
