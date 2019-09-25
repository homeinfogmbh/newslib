"""Object-relational mappings."""

from peewee import ForeignKeyField

from mdb import Customer
from peeweeplus import EnumField, JSONModel, MySQLDatabase

from newslib.config import CONFIG
from newslib.enumerations import Provider


__all__ = ['CustomerProvider']


DATABASE = MySQLDatabase.from_config(CONFIG['db'])


class NewslibModel(JSONModel):
    """Base model for the news library database."""

    class Meta:     # pylint: disable=C0111,R0903
        database = DATABASE
        schema = database.database


class CustomerProvider(NewslibModel):
    """Whitelist of news providers for customers."""

    class Meta:     # pylint: disable=C0111,R0903
        table_name = 'customer_provider'

    customer = ForeignKeyField(
        Customer, column_name='customer', on_delete='CASCADE',
        on_update='CASCADE')
    provider = EnumField(Provider)

    @classmethod
    def from_json(cls, json, customer=None, unique=False, **kwargs):
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
