from typing import List
from decimal import Decimal
from .types import Receive, Sale


def calculate_wac(receives: List[Receive]) -> Decimal:
    """Calculates the weighted average cost given a list of receives"""
    cost = sum([r.cost * r.quantity for r in receives])
    quantity = sum([r.quantity for r in receives])

    return cost / quantity


def calculate_profit(sales: List[Sale], wac: Decimal) -> Decimal:
    """Calculates profit given a list of sales and a WAC"""
    return sum([(sale.price - wac) * sale.quantity for sale in sales])


def calculate_unsold_stock_cost(unsold_units: int, wac: Decimal) -> Decimal:
    """Calculates the value of the unsold stock given a count of unsold units and a WAC"""
    return unsold_units * wac
