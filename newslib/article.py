"""Conversion from news from welt.de."""

from __future__ import annotations
from datetime import datetime
from logging import getLogger
from typing import Any, NamedTuple, Optional

from filedb import File
from ferengi import googlenews, spiegelnews, weltnews

from newslib import dom
from newslib.enumerations import Provider


__all__ = ['Article']


LOGGER = getLogger(__file__)


class Article(NamedTuple):
    """Represents an article."""

    provider: Provider
    title: str
    subtitle: Optional[str]
    text: str
    source: str
    author: Optional[str]
    published: datetime
    image: File

    @classmethod
    def from_google(cls, news: googlenews.News) -> Article:
        """Returns an article from a Google News RSS feed entry."""
        return cls(
            Provider.GOOGLE, news.title, None, news.text, news.source,
            news.author, news.published, news.image
        )

    @classmethod
    def from_spiegel(cls, news: spiegelnews.News):
        """Returns an article from a Spiegel.de news entry."""
        return cls(
            Provider.SPIEGEL, news.title, None, news.text, news.source,
            news.author, news.published, news.image
        )

    @classmethod
    def from_welt(cls, news: weltnews.News):
        """Returns an article / attachment data
        pair for a welt.de news record.
        """
        return cls(
            Provider.WELT, news.headline, news.subline, news.textmessage,
            news.source, None, news.published, news.image
        )

    def to_dom(self):
        """Returns an article as a DOM model."""
        article: Any = dom.Article()
        article.provider = self.provider.value
        article.title = self.title
        article.subtitle = self.subtitle
        article.text = self.text
        article.source = self.source
        article.author = self.author
        article.published = self.published

        if self.image:
            article.image = dom.Attachment(
                self.image.filename, mimetype=self.image.mimetype,
                sha256sum=self.image.sha256sum, id=self.image.id
            )

        return article
