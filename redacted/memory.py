from collections import defaultdict
from typing import List, Set, Dict
from .types import Sale, Sku, Receive


_RECEIVE = []
_SALES = []


def _reset() -> None:
    """Cleans the store. Only for testing."""
    global _RECEIVE
    global _SALES

    _RECEIVE = []
    _SALES = []


def _get_skus_stock_count() -> Dict[Sku, int]:
    """Returns the availability of all SKUs. Guaranteed to not return zero or negative counts"""
    counts = defaultdict(lambda: 0)

    for receive in _RECEIVE:
        counts[receive.sku] += receive.quantity

    for sale in _SALES:
        counts[sale.sku] -= sale.quantity

    return {sku: count for sku, count in counts.items() if count > 0}


def put_receive(request: Receive) -> None:
    """Stores a receive request"""
    _RECEIVE.append(request)


def get_receives(sku: Sku) -> List[Receive]:
    """Returns all the receives for a given SKU"""
    return [request for request in _RECEIVE if sku in request.sku]


def put_sale(sale: Sale) -> None:
    """Stores a sale"""
    _SALES.append(sale)


def get_sales(sku: Sku) -> List[Sale]:
    """Returns all the sales for a given SKU"""
    return [sale for sale in _SALES if sku in sale.sku]


def get_skus() -> Set[Sku]:
    """Returns all the SKUs with >= 1 units"""
    counts = _get_skus_stock_count()

    return set(counts.keys())


def get_sku_availability(sku: Sku) -> int:
    """Returns the number of units ready to be sold for a given SKU. Throws if SKU is not present"""
    counts = _get_skus_stock_count()

    if sku not in counts:
        raise ValueError('SKU not in inventory')

    return counts[sku]


def get_sku_sales_count(sku: Sku) -> int:
    """Returns the number of units sold for a given SKU"""
    return sum([sale.quantity for sale in _SALES if sku in sale.sku])
