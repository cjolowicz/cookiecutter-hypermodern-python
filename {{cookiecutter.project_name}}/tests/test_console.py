"""Test cases for the console module."""
from click.testing import CliRunner
import pytest

from {{cookiecutter.package_name}} import console


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0
