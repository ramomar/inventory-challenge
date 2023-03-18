from decimal import Decimal
from redacted.types import Receive, Sale
from redacted import memory


def test_get_sku_sales_count(reset_memory):
    """it should return the correct number of units sold"""
    sku = 'SNOWFLAKES'
    receive_requests = [
        Receive(sku=sku, quantity=8, cost=Decimal(1.00)),
        Receive(sku=sku, quantity=2, cost=Decimal(3.50))
    ]
    sales = [
        Sale(sku=sku, quantity=2, price=Decimal(2.50)),
    ]

    for receive in receive_requests:
        memory.put_receive(receive)

    for sale in sales:
        memory.put_sale(sale)

    expected = 2
    actual = memory.get_sku_sales_count(sku)

    assert actual == expected


def test_get_sku_availability(reset_memory):
    """it should return the correct number of units available for sale"""
    sku = 'SNOWFLAKES'
    receive_requests = [
        Receive(sku=sku, quantity=8, cost=Decimal(1.00)),
        Receive(sku=sku, quantity=2, cost=Decimal(3.50))
    ]
    sales = [
        Sale(sku=sku, quantity=2, price=Decimal(2.50)),
    ]

    for receive in receive_requests:
        memory.put_receive(receive)

    for sale in sales:
        memory.put_sale(sale)

    expected = 8
    actual = memory.get_sku_availability(sku)

    assert actual == expected


def test_get_skus(reset_memory):
    """it should return all the SKUs ready to be sold (>= 1 unit)"""
    sku = 'SNOWFLAKES'
    sku_2 = 'COOKIES'
    receive_requests = [
        Receive(sku=sku, quantity=8, cost=Decimal(1.00)),
        Receive(sku=sku_2, quantity=2, cost=Decimal(3.50))
    ]
    sales = [
        Sale(sku=sku_2, quantity=2, price=Decimal(2.50)),
    ]

    for receive in receive_requests:
        memory.put_receive(receive)

    for sale in sales:
        memory.put_sale(sale)

    expected = {sku}
    actual = memory.get_skus()

    assert actual == expected


def test_get_sales(reset_memory):
    """it should return all the sales for a given SKU"""
    sku = 'SNOWFLAKES'
    sku_2 = 'COOKIES'
    receive_requests = [
        Receive(sku=sku, quantity=8, cost=Decimal(1.00)),
        Receive(sku=sku_2, quantity=2, cost=Decimal(3.50))
    ]
    sales = [
        Sale(sku=sku, quantity=2, price=Decimal(1.00)),
        Sale(sku=sku_2, quantity=2, price=Decimal(2.50)),
    ]

    for receive in receive_requests:
        memory.put_receive(receive)

    for sale in sales:
        memory.put_sale(sale)

    expected = [Sale(sku=sku_2, quantity=2, price=Decimal(2.50))]
    actual = memory.get_sales(sku_2)

    assert actual == expected


def test_get_receive(reset_memory):
    """it should return all the receives for a given SKU"""
    sku = 'SNOWFLAKES'
    sku_2 = 'COOKIES'
    receive_requests = [
        Receive(sku=sku, quantity=8, cost=Decimal(1.00)),
        Receive(sku=sku, quantity=20, cost=Decimal(1.00)),
        Receive(sku=sku_2, quantity=2, cost=Decimal(3.50))
    ]
    sales = [
        Sale(sku=sku, quantity=2, price=Decimal(1.00)),
        Sale(sku=sku_2, quantity=2, price=Decimal(2.50)),
    ]

    for receive in receive_requests:
        memory.put_receive(receive)

    for sale in sales:
        memory.put_sale(sale)

    expected = [
        Receive(sku=sku, quantity=8, cost=Decimal(1.00)),
        Receive(sku=sku, quantity=20, cost=Decimal(1.00)),
    ]
    actual = memory.get_receives(sku)

    assert actual == expected
