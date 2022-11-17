"""Common enumerations."""

from enum import Enum


__all__ = ['Provider']


class Provider(Enum):
    """Enumeration of available news providers."""

    DPA = 'DPA'
    HOMEINFO = 'HOMEINFO'
    SPIEGEL = 'spiegel.de'
    WELT = 'welt.de'
