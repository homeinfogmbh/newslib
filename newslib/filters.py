"""Article filtering."""

from typing import Iterator, Optional, Union

from ferengi import googlenews, spiegelnews, weltnews
from mdb import Customer

from newslib.article import Article
from newslib.enumerations import Provider
from newslib.orm import CustomerProvider


__all__ = ['articles']


GOOGLE_PROVIDERS = {
    Provider.GOOGLE_BGW_BIELEFELD_FACEBOOK,
    Provider.GOOGLE_BGW_BIELEFELD_WEBSITE,
    Provider.GOOGLE_HANNOVER,
    Provider.GOOGLE_HANNOVER_INSTAGRAM,
    Provider.GOOGLE_WUERZBURG,
    Provider.GOOGLE_WGH_HERRENHAUSEN_FACEBOOK
}


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

    # Process Google news.
    for provider in GOOGLE_PROVIDERS:
        if provider in providers:
            for article in googlenews.News.select().where(
                    googlenews.News.source == googlenews.FEEDS[
                        provider.value.replace('Google RSS', '').strip()
                    ]
            ):
                yield Article.from_google(provider, article)

    # Process spiegel.de news.
    if Provider.SPIEGEL in providers:
        for article in spiegelnews.News.select().where(True):
            yield Article.from_spiegel(article)

    # Process welt.de news.
    if Provider.WELT in providers:
        for article in weltnews.News.select().where(True):
            yield Article.from_welt(article)
