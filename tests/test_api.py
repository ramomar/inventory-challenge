import pytest
from decimal import Decimal
from redacted.types import Sale, Receive
import redacted.api as api


def test_sell_not_in_inventory(reset_memory):
    """it should throw when the SKU is not in the inventory"""
    with pytest.raises(ValueError) as excinfo:
        api.sell(Sale(sku='CORNFLAKES', quantity=2, price=Decimal(2.50)))

    assert 'SKU not in inventory' in str(excinfo)


def test_sell_not_enough_quantity(reset_memory):
    """it should throw when trying to sell more stock that what's available in the inventory"""
    api.receive(Receive(sku='SNOWFLAKES', quantity=8, cost=Decimal(1.00)))

    with pytest.raises(ValueError) as excinfo:
        api.sell(Sale(sku='SNOWFLAKES', quantity=1000, price=Decimal(2.50)))

    assert 'Cannot sell stock: 8' in str(excinfo)
