"""
Top-level package for the 2D Gaussian Splatting utilities.

The distribution is published as ``2dgs`` on PyPI/Git, but the importable
module is named ``twodgs`` because Python identifiers cannot begin with a
number.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("2dgs")
except PackageNotFoundError:  # pragma: no cover - local editable installs
    __version__ = "0.0.0"

__all__ = ["__version__"]
