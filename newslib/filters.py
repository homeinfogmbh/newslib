"""Article filtering."""

from typing import Iterator, Optional, Union

from ferengi import rssapp, spiegelnews, weltnews
from mdb import Customer

from newslib.article import Article
from newslib.enumerations import Provider
from newslib.orm import CustomerProvider


__all__ = ['articles']


def _customer_providers(customer: Union[Customer, int]) -> Iterator[str]:
    """Yields the providers of the respective customer."""

    for provider in CustomerProvider.select().where(
            CustomerProvider.customer == customer
    ):
        yield provider.provider


def _get_providers(
        customer: Union[Customer, int],
        wanted_providers: Optional[set[str]]
) -> set[str]:
    """Returns the news providers dict."""

    providers = set(_customer_providers(customer))

    if wanted_providers is not None:
        providers &= wanted_providers

    return providers


def articles(
        customer: Union[Customer, int],
        wanted_providers: Optional[set[Provider]] = None
) -> Iterator[Article]:
    """Yields the respective articles."""

    providers = _get_providers(customer, wanted_providers)

    for article in rssapp.News.select(rssapp.News, rssapp.Provider).join(
            rssapp.Provider,
            on=rssapp.News.source == rssapp.Provider.url
    ).where(
            rssapp.Provider.name << providers
    ).iterator():
        yield Article.from_rssapp(article.provider.name, article)

    # Process spiegel.de news.
    if Provider.SPIEGEL in providers:
        for article in spiegelnews.News.select().where(True).iterator():
            yield Article.from_spiegel(article)

    # Process welt.de news.
    if Provider.WELT in providers:
        for article in weltnews.News.select().where(True).iterator():
            yield Article.from_welt(article)
