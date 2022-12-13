"""Common enumerations."""

from enum import Enum


__all__ = ['Provider']


class Provider(str, Enum):
    """Enumeration of available news providers."""

    RSS_APP_HANNOVER = 'RSS.APP Hannover'
    RSS_APP_WUERZBURG = 'RSS.APP Würzburg'
    RSS_APP_BGW_BIELEFELD_FACEBOOK = 'RSS.APP BGW Bielefeld Facebook'
    RSS_APP_HANNOVER_INSTAGRAM = 'RSS.APP #hannover on Instagram'
    RSS_APP_WGH_HERRENHAUSEN_FACEBOOK = 'RSS.APP WGH Herrenhausen Facebook'
    RSS_APP_BGW_BIELEFELD_WEBSITE = 'RSS.APP BGW Bielefeld Website'
    SPIEGEL = 'spiegel.de'
    WELT = 'welt.de'
