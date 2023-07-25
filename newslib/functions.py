"""Common functions."""

from typing import Iterator

from ferengi import rssapp

from newslib.enumerations import Provider


__all__ = ["list_providers"]


def list_providers() -> Iterator[str]:
    """Yield provider names."""

    for provider in Provider:
        yield provider.value

    for provider in rssapp.Provider.select().where(True):
        yield provider.name
