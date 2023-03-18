from decimal import Decimal
from redacted.types import Receive, Sale
from redacted import logic


def test_calculate_wac():
    """it should calculate the correct wac"""
    receive_requests = [
        Receive(sku='SNOWFLAKES', quantity=8, cost=Decimal(1.00)),
        Receive(sku='SNOWFLAKES', quantity=2, cost=Decimal(3.50))
    ]
    actual = logic.calculate_wac(receive_requests)
    expected = Decimal(1.50)

    assert actual == expected


def test_calculate_profit():
    """it should calculate the profit given a WAC"""
    sales = [
        Sale(sku='SNOWFLAKES', quantity=2, price=Decimal(2.50)),
        Sale(sku='SNOWFLAKES', quantity=4, price=Decimal(3.00))
    ]
    wac = Decimal(1.50)
    actual = logic.calculate_profit(sales, wac)
    expected = Decimal(8.00)

    assert actual == expected


def test_calculate_unsold_stock_cost():
    """it should calculate the value of unsold stock"""
    unsold_units = 4
    wac = Decimal(2.50)
    actual = logic.calculate_unsold_stock_cost(unsold_units, wac)
    expected = Decimal(10)

    assert actual == expected
