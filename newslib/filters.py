"""Article filtering."""

from ferengi.weltnews import News
from hinews import article_active, Article as HomeinfoArticle

from newslib.article import Article
from newslib.enumerations import Provider
from newslib.orm import CustomerProvider


__all__ = ['articles']


def _customer_providers(customer):
    """Yields the providers of the respective customer."""

    for provider in CustomerProvider.select().where(
            CustomerProvider.customer == customer):
        yield provider.provider


def articles(customer, wanted_providers=None):
    """Yields the respective articles."""

    providers = set(_customer_providers(customer))

    if wanted_providers is not None:
        providers &= wanted_providers

    # Process HOMEINFO news.
    if Provider.HOMEINFO in providers:
        for article in HomeinfoArticle.select().where(article_active()):
            customers = article.customers

            if not customers or customer in customers:
                yield Article.from_homeinfo(article)

    # Process welt.de news.
    if Provider.WELT in providers:
        for article in News.select().where(True):
            yield Article.from_welt(article)
