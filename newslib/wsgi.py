"""Administrative interface to enable news providers for customers."""

from flask import request

from his import CUSTOMER, authenticated, authorized, root, Application
from mdb import Customer
from wsgilib import JSON

from newslib.enumerations import Provider
from newslib.messages import NO_CUSTOMER_SPECIFIED
from newslib.messages import NO_SUCH_CUSTOMER
from newslib.messages import CUSTOMER_PROVIDER_ADDED
from newslib.messages import NO_SUCH_CUSTOMER_PROVIDER
from newslib.messages import CUSTOMER_PROVIDER_DELETED
from newslib.orm import CustomerProvider


__all__ = ['APPLICATION']


APPLICATION = Application('news')


@authenticated
@root
def list_providers():
    """Lists customer providers."""

    return JSON([provider.value for provider in Provider])


@authenticated
@authorized('news')
def list_customer_providers():
    """Lists customer providers."""

    return JSON([
        customer_provider.to_json() for customer_provider
        in CustomerProvider.select().where(
            CustomerProvider.customer == CUSTOMER.id)])


@authenticated
@root
def add_customer_provider():
    """Adds a new customer provider."""

    try:
        customer = Customer[request.json.pop('customer')]
    except (KeyError, TypeError):
        raise NO_CUSTOMER_SPECIFIED
    except Customer.DoesNotExist:
        raise NO_SUCH_CUSTOMER

    customer_provider = CustomerProvider.from_json(
        request.json, customer=customer)
    customer_provider.save()
    return CUSTOMER_PROVIDER_ADDED.update(id=customer_provider.id)


@authenticated
@root
def delete_customer_provider(ident):
    """Removes the respective customer provider."""

    try:
        customer_provider = CustomerProvider[ident]
    except CustomerProvider.DoesNotExist:
        raise NO_SUCH_CUSTOMER_PROVIDER

    customer_provider.delete_instance()
    return CUSTOMER_PROVIDER_DELETED


APPLICATION.add_routes((
    ('GET', '/providers', list_providers),
    ('GET', '/customer-providers', list_customer_providers),
    ('POST', '/customer-providers', add_customer_provider),
    ('DELETE', '/customer-provider/<int:ident>', delete_customer_provider)
))
