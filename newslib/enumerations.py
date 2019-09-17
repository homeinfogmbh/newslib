"""Common enumerations."""

from enum import Enum


__all__ = ['Provider']


class Provider(Enum):
    """Enumeration of available news providers."""

    HOMEINFO = 'HOMEINFO'
    WELT = 'welt.de'
    DPA = 'DPA'
