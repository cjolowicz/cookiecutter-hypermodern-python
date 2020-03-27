"""Nox sessions."""
import nox
from nox.sessions import Session


@nox.session
def docs(session: Session) -> None:
    """Build the documentation."""
    session.install("sphinx", "recommonmark")
    session.run("sphinx-build", "docs", "docs/_build")
