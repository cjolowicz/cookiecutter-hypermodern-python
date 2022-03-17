"""Test cases for the __main__ module."""
from __future__ import annotations

from typing import TYPE_CHECKING

from {{cookiecutter.package_name}} import __main__


if TYPE_CHECKING:
    from click.testing import CliRunner


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 0
