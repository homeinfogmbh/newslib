"""Conversion from news from welt.de."""

from newslib.dom import Article, Attachment

from filedb import get
from mimeutil import FileMetaData


__all__ = ['welt_to_dom']


def welt_to_dom(record):
    """Returns a welt.de news record into the centralized XML format."""

    article = Article()
    article.title = record.headline
    article.subtitle = record.subline
    article.text = record.textmessage
    article.source = record.source

    if record.image is not None:
        bytes_ = get(record.image)
        file_meta_data = FileMetaData.from_bytes(bytes_)
        article.image = Attachment(
            file_meta_data.filename, mimetype=file_meta_data.mimetype,
            id=record.image)

    article.published = record.published
    return article
