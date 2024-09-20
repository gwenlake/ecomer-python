import os
from importlib import metadata

try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""

from ecomer.client import Client


__all__ = [
    "__version__",
    "Client",
]
