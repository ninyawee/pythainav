import importlib
import types
from typing import Optional


def import_optional_dependency(
    name: str,
    extra: str = "",
    raise_on_missing: bool = True,
) -> Optional[types.ModuleType]:
    """Import an optional dependency.

    By default, if the dependency is missing an ``ImportError`` with a helpful
    message is raised. When ``raise_on_missing`` is False and the module is not
    present, ``None`` is returned instead.
    """
    try:
        return importlib.import_module(name)
    except ImportError as err:
        if not raise_on_missing:
            return None
        msg = (
            f"Missing optional dependency '{name}'. {extra} "
            f"Use pip or uv to install {name}."
        )
        raise ImportError(msg) from err
