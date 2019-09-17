"""Common configuration parsing."""

from configlib import loadcfg


__all__ = ['CONFIG']


CONFIG = loadcfg('newslib.conf')
