# pcost.py
#
# Exercise 1.27

#def portfolio_cost(filename):
#    total_cost = 0
#    with open(filename, 'rt') as file: 
#        # csv heading - stock name, number of shares, purchase price
#        headers = next(file)
#        for line in file: 
#            row = line.split(',')
#            try: 
#                ticker, shares, price = row[0], int(row[1]), float(row[2])
#                total_cost += (shares * price) 
#            except (IndexError, ValueError) as e: 
#                print("Couldn't parse", line)
#    return total_cost
#    
#print('Total cost', portfolio_cost('Data/portfolio.csv'))

# Exercise 1.32

import csv 
import sys 

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as file: 
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows: 
            try: 
                nshares = int(row[1])
                price = float(row[2])
                total_cost += (price * nshares)
            except (ValueError, IndexError):
                print("Couldn't parse", row)
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else: 
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
