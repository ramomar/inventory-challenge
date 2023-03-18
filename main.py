from decimal import Decimal
from redacted.types import Receive, Sale, SkuReport
import redacted.api as api


def _format_report(report: SkuReport) -> str:
    return '\n'.join([
        f'{report.sold_quantity} units of “{report.sku}” have been sold',
        f'{report.unsold_quantity} units of “{report.sku}” are currently in stock',
        f'{"Profit" if report.profit > 0 else "Loss"}: {report.profit}:',
        f'Unsold stock cost: {report.unsold_stock_cost}'
    ])


def profit_scenario():
    receive_requests = [
        Receive(sku='SNOWFLAKES', quantity=8, cost=Decimal(1.00)),
        Receive(sku='SNOWFLAKES', quantity=2, cost=Decimal(3.50))
    ]

    sales = [
        Sale(sku='SNOWFLAKES', quantity=2, price=Decimal(2.50)),
        Sale(sku='SNOWFLAKES', quantity=4, price=Decimal(3.00))
    ]

    for request in receive_requests:
        api.receive(request)

    for sale in sales:
        api.sell(sale)

    report = api.report()

    for report in report.reports:
        print(_format_report(report))


def loss_scenario():
    receive_requests = [
        Receive(sku='SNOWFLAKES', quantity=8, cost=Decimal(5.00)),
        Receive(sku='SNOWFLAKES', quantity=2, cost=Decimal(5.00))
    ]

    sales = [
        Sale(sku='SNOWFLAKES', quantity=2, price=Decimal(0.50)),
        Sale(sku='SNOWFLAKES', quantity=4, price=Decimal(0.50))
    ]

    for request in receive_requests:
        api.receive(request)

    for sale in sales:
        api.sell(sale)

    report = api.report()

    for report in report.reports:
        print(_format_report(report))


if __name__ == '__main__':
    print('Profit scenario')
    profit_scenario()

    print('\nLoss scenario\n')
    api.reset()
    loss_scenario()
