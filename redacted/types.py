from dataclasses import dataclass
from typing import List
from decimal import Decimal

Sku = str
SaleId = str


@dataclass(frozen=True)
class Sale:
    sku: Sku
    price: Decimal
    quantity: int


@dataclass(frozen=True)
class Receive:
    sku: Sku
    quantity: int
    cost: Decimal


@dataclass(frozen=True)
class SellRequest:
    sku: Sku
    quantity: int
    price: int


@dataclass(frozen=True)
class SkuReport:
    sku: Sku
    unsold_stock_cost: Decimal
    profit: Decimal
    sold_quantity: int
    unsold_quantity: int


@dataclass(frozen=True)
class Report:
    reports: List[SkuReport]
