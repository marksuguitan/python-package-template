"""Top-level package for {{ cookiecutter.project_name }}."""

from .core import hello
from ._version import __version__  # Assuming _version.py exists

__all__ = ["hello", "__version__"]
