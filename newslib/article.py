"""Conversion from news from welt.de."""

from datetime import datetime
from logging import getLogger
from typing import NamedTuple

from filedb import FileError, get
from hinews.orm import Image
from mimeutil import FileMetaData

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
    image: int

    @classmethod
    def from_homeinfo(cls, article):
        """Returns a new article from a HOMEINFO News article."""
        try:
            image = article.images.get()
        except Image.DoesNotExist:
            image = None
        else:
            image = image._file     # pylint: disable=W0212

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

    @property
    def attachment_bytes(self):
        """Returns the bytes of the respective attachment."""
        if self.image is None:
            raise ValueError('No attachment set.')

        return get(self.image)

    @property
    def attachment_dom(self):
        """Returns the attachment DOM."""
        if not self.image:
            return None

        try:
            metadata = FileMetaData.from_bytes(self.attachment_bytes)
        except FileError:
            LOGGER.error('Could not retrieve file %i.', self.image)

        return Attachment(
            metadata.filename, mimetype=metadata.mimetype,
            sha256sum=metadata.sha256sum, id=self.image)

    def to_dom(self):
        """Returns an article as a DOM model."""
        article = ArticleDOM()
        article.provider = self.provider.value
        article.title = self.title
        article.subtitle = self.subtitle
        article.text = self.text
        article.source = self.source
        article.published = self.published
        article.image = self.attachment_dom
        return article
