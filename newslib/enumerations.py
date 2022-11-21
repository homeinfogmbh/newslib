"""Common enumerations."""

from enum import Enum


__all__ = ['Provider']


class Provider(str, Enum):
    """Enumeration of available news providers."""

    DPA = 'DPA'
    GOOGLE = 'google.com'
    HOMEINFO = 'HOMEINFO'
    SPIEGEL = 'spiegel.de'
    WELT = 'welt.de'
