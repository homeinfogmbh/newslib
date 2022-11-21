"""Article filtering."""

from typing import Iterator, Optional, Union

from ferengi import googlenews, spiegelnews, weltnews
from mdb import Customer
import hinews

from newslib.article import Article
from newslib.enumerations import Provider
from newslib.orm import CustomerProvider


__all__ = ['articles']


def _customer_providers(customer: Union[Customer, int]) -> Iterator[Provider]:
    """Yields the providers of the respective customer."""

    for provider in CustomerProvider.select().where(
            CustomerProvider.customer == customer
    ):
        yield provider.provider


def articles(
        customer: Union[Customer, int],
        wanted_providers: Optional[set[Provider]] = None
) -> Iterator[Article]:
    """Yields the respective articles."""

    providers = set(_customer_providers(customer))

    if wanted_providers is not None:
        providers &= wanted_providers

    # Process spiegel.de news.
    if Provider.GOOGLE in providers:
        for article in googlenews.News.select().where(True):
            yield Article.from_spiegel(article)

    # Process HOMEINFO news.
    if Provider.HOMEINFO in providers:
        for article in hinews.Article.select().where(hinews.article_active()):
            customers = article.customers

            if not customers or customer in customers:
                yield Article.from_homeinfo(article)

    # Process spiegel.de news.
    if Provider.SPIEGEL in providers:
        for article in spiegelnews.News.select().where(True):
            yield Article.from_spiegel(article)

    # Process welt.de news.
    if Provider.WELT in providers:
        for article in weltnews.News.select().where(True):
            yield Article.from_welt(article)
