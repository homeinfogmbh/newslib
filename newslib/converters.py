"""Conversion from news from welt.de."""

from filedb import get
from mimeutil import FileMetaData

from newslib.dom import Article, Attachment
from newslib.enumerations import Provider


__all__ = ['homeinfo_to_dom', 'welt_to_dom']


def homeinfo_to_dom(record):
    """Returns an article / attachment data
    pair for a HOMEINFO news record.
    """

    article = Article()
    article.provider = Provider.HOMEINFO.value
    article.title = record.title
    article.subtitle = record.subtitle
    article.text = record.text
    article.source = record.source
    article.published = record.created

    for image in record.images:
        try:
            bytes_ = image.watermarked
        except OSError:
            continue
        else:
            break
    else:
        bytes_ = None

    if bytes_:
        file_meta_data = FileMetaData.from_bytes(bytes_)
        article.image = Attachment(
            file_meta_data.filename, mimetype=file_meta_data.mimetype,
            id=record.image)

    return (article, bytes_)


def welt_to_dom(record):
    """Returns an article / attachment data
    pair for a welt.de news record.
    """

    article = Article()
    article.provider = Provider.WELT.value
    article.title = record.headline
    article.subtitle = record.subline
    article.text = record.textmessage
    article.source = record.source
    article.published = record.published

    if record.image is not None:
        bytes_ = get(record.image)
        file_meta_data = FileMetaData.from_bytes(bytes_)
        article.image = Attachment(
            file_meta_data.filename, mimetype=file_meta_data.mimetype,
            id=record.image)

    return (article, bytes_)
