"""Object-relational mappings."""

from __future__ import annotations
from typing import Optional, Union

from peewee import ForeignKeyField

from mdb import Customer
from peeweeplus import EnumField, JSONModel, MySQLDatabaseProxy

from newslib.enumerations import Provider


__all__ = ['CustomerProvider']


DATABASE = MySQLDatabaseProxy('newslib')


class NewslibModel(JSONModel):
    """Base model for the news library database."""

    class Meta:
        database = DATABASE
        schema = database.database


class CustomerProvider(NewslibModel):
    """Whitelist of news providers for customers."""

    class Meta:
        table_name = 'customer_provider'

    customer = ForeignKeyField(
        Customer, column_name='customer', on_delete='CASCADE',
        on_update='CASCADE'
    )
    provider = EnumField(Provider)

    @classmethod
    def from_json(
            cls,
            json: dict,
            customer: Optional[Union[Customer, int]] = None,
            unique: bool = False,
            **kwargs
    ) -> CustomerProvider:
        """Returns a new customer provider from a JSON-ish dict."""
        record = super().from_json(json, **kwargs)
        record.customer = customer

        if not unique:
            return record

        if customer is None:
            raise ValueError('Cannot add unique entry without customer.')

        try:
            return cls.get(
                (cls.customer == customer) & (cls.provider == record.provider))
        except cls.DoesNotExist:
            return record
