"""Nox sessions."""
from pathlib import Path
import shutil

import nox
from nox.sessions import Session


@nox.session
def docs(session: Session) -> None:
    """Build the documentation."""
    args = session.posargs or ["docs", "docs/_build"]

    if session.interactive and not session.posargs:
        args.append("--open-browser")

    builddir = Path("docs", "_build")
    if builddir.exists():
        shutil.rmtree(builddir)

    session.install("sphinx", "sphinx-autobuild", "recommonmark")

    if session.interactive:
        session.run("sphinx-autobuild", *args)
    else:
        session.run("sphinx-build", *args)
