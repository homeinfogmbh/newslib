"""Non-authenticated WSGI interface.

XXX: For internal use only!
"""
from typing import Union

from flask import request

from wsgilib import Application, JSON, JSONMessage

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

    if not (customer := request.json.get('customer')):
        return JSONMessage('No customer specified.')

    if providers := request.json.get('providers'):
        providers = set(providers)
    else:
        providers = None

    return JSON([
        article.to_json() for article
        in articles(customer, providers)
    ])
