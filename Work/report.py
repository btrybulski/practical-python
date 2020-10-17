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

if __name__ == "__main__":
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    total_cost = 0.0
    for record in portfolio: 
        total_cost += record['shares'] * record['price']
    
    total_value = 0.0 
    for record in portfolio: 
        total_value += record['shares'] * prices[record['name']]
    
    print('Total cost', total_cost)
    print('Total value', total_value)
    print('Profit', round(total_value - total_cost, ndigits=2))
