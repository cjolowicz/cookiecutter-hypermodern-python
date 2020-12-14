"""Nox sessions."""
from pathlib import Path
import shutil

import nox
from nox.sessions import Session

nox.options.sessions = (
    "linkcheck",
)

@nox.session
def docs(session: Session) -> None:
    """Build the documentation."""
    args = session.posargs or ["-W", "-n", "docs", "docs/_build"]

    if session.interactive and not session.posargs:
        args = ["-a", "--watch=docs/_static", "--open-browser", *args]

    builddir = Path("docs", "_build")
    if builddir.exists():
        shutil.rmtree(builddir)

    session.install("-r", "docs/requirements.txt")

    if session.interactive:
        session.run("sphinx-autobuild", *args)
    else:
        session.run("sphinx-build", *args)

@nox.session
def linkcheck(session: Session) -> None:
    """Build the documentation."""
    args = session.posargs or ["-W", "-b", "linkcheck", "docs", "docs/_build"]

    builddir = Path("docs", "_build")
    if builddir.exists():
        shutil.rmtree(builddir)

    session.install("-r", "docs/requirements.txt")

    session.run("sphinx-build", *args)
