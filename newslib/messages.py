"""WSGI messages."""

from wsgilib import JSONMessage


__all__ = [
    "NO_CUSTOMER_SPECIFIED",
    "NO_SUCH_CUSTOMER",
    "CUSTOMER_PROVIDER_ADDED",
    "NO_SUCH_CUSTOMER_PROVIDER",
    "CUSTOMER_PROVIDER_DELETED",
]


NO_CUSTOMER_SPECIFIED = JSONMessage("No customer specified.", 400)
NO_SUCH_CUSTOMER = JSONMessage("No such customer.", 404)
CUSTOMER_PROVIDER_ADDED = JSONMessage("Customer provider added.", 201)
NO_SUCH_CUSTOMER_PROVIDER = JSONMessage("No such customer provider.", 404)
CUSTOMER_PROVIDER_DELETED = JSONMessage("Customer provider deleted.", 200)
