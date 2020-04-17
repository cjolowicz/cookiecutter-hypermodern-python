"""{{cookiecutter.friendly_name}}."""
import sys

if sys.version_info[:2] >= (3, 8):
    from importlib.metadata import version, PackageNotFoundError  # pragma: no cover
else:
    from importlib_metadata import version, PackageNotFoundError  # pragma: no cover


try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
