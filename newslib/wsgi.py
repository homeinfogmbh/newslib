"""Non-authenticated WSGI interface.

XXX: For internal use only!
"""
from typing import Iterator, Union

from flask import request

from filedb import File
from wsgilib import Application, Binary, JSON, JSONMessage

from newslib.article import Article
from newslib.filters import articles
from newslib.functions import list_providers


__all__ = ['APPLICATION']


APPLICATION = Application('news', cors=True)


@APPLICATION.route('/', methods=['GET'], strict_slashes=False)
def _list_providers() -> JSON:
    """List available news providers."""

    return JSON(list(list_providers()))


@APPLICATION.route('/', methods=['POST'], strict_slashes=False)
def _get_articles() -> Union[JSON, JSONMessage]:
    """Return articles of the requested customer and providers."""

    return JSON([article.to_json() for article in requested_articles()])


@APPLICATION.route('/<sha256sum>', methods=['POST'], strict_slashes=False)
def _get_image(sha256sum: str) -> Union[Binary, JSONMessage]:
    """Return the requested image for a given customer and providers."""

    images = {
        article.image.sha256sum: article.image
        for article in requested_articles()
        if article.image
    }

    try:
        file = File.get(File.id == images[sha256sum].id).bytes
    except (KeyError, File.DoesNotExist):
        return JSONMessage('No such image.', status=404)

    return Binary(file.bytes, filename=file.filename)


def requested_articles() -> Iterator[Article]:
    """Yield articles for the current customer and providers."""

    if not (customer := request.json.get('customer')):
        raise JSONMessage('No customer specified.', status=400)

    if providers := request.json.get('providers'):
        return articles(customer, set(providers))

    return articles(customer)
