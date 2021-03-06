# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(holding)
    return portfolio

## bonus - think about how you could rewrite it with this pattern
##headers = ['name','price','date','time','change','open','high','low','volume']
##types = [str, float, str, str, float, float, float, float, int]
##converted = [func(val) for func, val in zip(types, row)]
##record = dict(zip(headers, converted))

def read_prices(filename):
    portfolio = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name = row[0]
                price = float(row[1])
                portfolio[name] = price
            except (ValueError, IndexError):
                print('Unable to parse row', row)
    return portfolio

def make_report(portfolio, prices):
    report = []
    for record in portfolio:
        name = record['name']
        shares = record['shares']
        price = record['price']
        change = prices[name] - price
        report.append((name, shares, price, change))
    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- -----------')
    for name, shares, price, change in report:
        price = '${:.2f}'.format(price)
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    total_cost = 0.0
    for record in portfolio:
       total_cost += record['shares'] * record['price']

    total_value = 0.0
    for record in portfolio:
       total_value += record['shares'] * prices[record['name']]

    print('Total cost', total_cost)
    print('Total value', total_value)
    print('Profit', round(total_value - total_cost, ndigits=2))
    print()

    report = make_report(portfolio, prices)
    print_report(report)

if __name__ == "__main__":
    portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
