"""Conversion from news from welt.de."""

from datetime import datetime
from logging import getLogger
from typing import NamedTuple

from filedb import META_FIELDS, File
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
    def attachment_metadata(self):
        """Returns the filedb.File."""
        if self.image is None:
            raise ValueError('No attachment set.')

        return File.select(*META_FIELDS).where(File.id == self.image).get()

    @property
    def attachment_dom(self):
        """Returns the attachment DOM."""
        if not self.image:
            return None

        try:
            file = self.attachment_metadata
        except File.DoesNotExist:
            LOGGER.error('Could not retrieve file %i.', self.image)
            return None

        return Attachment(
            file.filename, mimetype=file.mimetype, sha256sum=file.sha256sum,
            id=self.image)

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
