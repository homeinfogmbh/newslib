"""Centralized news library to accumulate news articles
from different sources into a centralized format.
"""

from newslib.converters import welt_to_dom
from newslib.orm import CustomerProvider


__all__ = ['welt_to_dom', 'CustomerProvider']
