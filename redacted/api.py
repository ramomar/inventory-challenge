from .types import Receive, Sale, Sku, SkuReport, Report
import redacted.logic as logic
import redacted.memory as mem


# Receive

def receive(rec: Receive) -> None:
    """Receive a request for storing units"""
    mem.put_receive(rec)


# Sell

def sell(sale: Sale) -> None:
    """Sell units. Throws if there's no available stock to be sold"""
    availability = mem.get_sku_availability(sale.sku)

    if sale.quantity > availability:
        raise ValueError(f'Cannot sell stock: {availability}')

    mem.put_sale(sale)


# Report

def _make_sku_report(sku: Sku) -> SkuReport:
    sales = mem.get_sales(sku)
    sold_stock_quantity = mem.get_sku_sales_count(sku)
    unsold_stock_quantity = mem.get_sku_availability(sku)
    receives = mem.get_receives(sku)
    wac = logic.calculate_wac(receives)
    profit = logic.calculate_profit(sales, wac)
    unsold_stock_cost = logic.calculate_unsold_stock_cost(unsold_stock_quantity, wac)

    return SkuReport(
        sku=sku,
        unsold_stock_cost=unsold_stock_cost,
        profit=profit,
        sold_quantity=sold_stock_quantity,
        unsold_quantity=unsold_stock_quantity
    )


def report() -> Report:
    """Make report for all SKUs"""
    skus = mem.get_skus()

    return Report(reports=[_make_sku_report(sku) for sku in skus])


def reset() -> None:
    mem._reset()
