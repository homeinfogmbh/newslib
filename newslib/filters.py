"""Article filtering."""

from typing import Iterator, Optional, Union

from ferengi import rssapp, spiegelnews, weltnews
from mdb import Customer

from newslib.article import Article
from newslib.enumerations import Provider
from newslib.orm import CustomerProvider


__all__ = ['articles']


RSS_APP_PROVIDERS = {
    Provider.RSS_APP_BGW_BIELEFELD_FACEBOOK,
    Provider.RSS_APP_BGW_BIELEFELD_WEBSITE,
    Provider.RSS_APP_HANNOVER,
    Provider.RSS_APP_HANNOVER_INSTAGRAM,
    Provider.RSS_APP_WUERZBURG,
    Provider.RSS_APP_WGH_HERRENHAUSEN_FACEBOOK
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

    # Process rss.app news.
    for provider in RSS_APP_PROVIDERS:
        if provider in providers:
            for article in rssapp.News.select().where(
                    rssapp.News.source == rssapp.FEEDS[
                        provider.value.replace('Google RSS', '').strip()
                    ]
            ):
                yield Article.from_rssapp(provider, article)

    # Process spiegel.de news.
    if Provider.SPIEGEL in providers:
        for article in spiegelnews.News.select().where(True):
            yield Article.from_spiegel(article)

    # Process welt.de news.
    if Provider.WELT in providers:
        for article in weltnews.News.select().where(True):
            yield Article.from_welt(article)
