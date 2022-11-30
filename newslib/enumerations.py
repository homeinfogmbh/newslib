"""Common enumerations."""

from enum import Enum


__all__ = ['Provider']


class Provider(str, Enum):
    """Enumeration of available news providers."""

    GOOGLE_HANNOVER = 'Google Hannover'
    GOOGLE_WUERZBURG = 'Google Würzburg'
    SPIEGEL = 'spiegel.de'
    WELT = 'welt.de'
