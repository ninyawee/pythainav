from importlib.metadata import PackageNotFoundError, version

from .api import get, get_all

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

__all__ = ["get", "get_all"]
