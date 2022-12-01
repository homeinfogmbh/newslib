"""Common enumerations."""

from enum import Enum


__all__ = ['Provider']


class Provider(str, Enum):
    """Enumeration of available news providers."""

    GOOGLE_HANNOVER = 'Google RSS Hannover'
    GOOGLE_WUERZBURG = 'Google RSS Würzburg'
    GOOGLE_BGW_BIELEFELD_FACEBOOK = 'Google RSS BGW Bielefeld Facebook'
    GOOGLE_HANNOVER_INSTAGRAM = 'Google RSS #hannover on Instagram'
    GOOGLE_WGH_HERRENHAUSEN_FACEBOOK = 'Google RSS WGH Herrenhausen Facebook'
    GOOGLE_BGW_BIELEFELD_WEBSITE = 'Google RSS BGW Bielefeld Website'
    SPIEGEL = 'spiegel.de'
    WELT = 'welt.de'
