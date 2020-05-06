"""Conversion from news from welt.de."""

from datetime import datetime
from logging import getLogger
from typing import NamedTuple

from filedb import File
from hinews.orm import Image

from newslib.dom import Article as ArticleDOM, Attachment
from newslib.enumerations import Provider


__all__ = ['Article']


LOGGER = getLogger(__file__)


class Article(NamedTuple):
    """Represents an article."""

    provider: Provider
    title: str
    subtitle: str
    text: str
    source: str
    published: datetime
    image: File

    @classmethod
    def from_homeinfo(cls, article):
        """Returns a new article from a HOMEINFO News article."""
        try:
            image = article.images.get()
        except Image.DoesNotExist:
            image = None
        else:
            image = image.file

        return cls(
            Provider.HOMEINFO, article.title, article.subtitle, article.text,
            article.source, article.created, image)

    @classmethod
    def from_welt(cls, news):
        """Returns an article / attachment data
        pair for a welt.de news record.
        """
        return cls(
            Provider.WELT, news.headline, news.subline, news.textmessage,
            news.source, news.published, news.image)

    def to_dom(self):
        """Returns an article as a DOM model."""
        article = ArticleDOM()
        article.provider = self.provider.value
        article.title = self.title
        article.subtitle = self.subtitle
        article.text = self.text
        article.source = self.source
        article.published = self.published

        if self.image:
            article.image = Attachment(
                self.image.filename, mimetype=self.image.mimetype,
                sha256sum=self.image.sha256sum, id=self.image.id)

        return article
