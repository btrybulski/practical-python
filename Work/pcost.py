# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as file: 
        # csv heading - stock name, number of shares, purchase price
        headers = next(file)
        for line in file: 
            row = line.split(',')
            try: 
                ticker, shares, price = row[0], int(row[1]), float(row[2])
                total_cost += (shares * price) 
            except (IndexError, ValueError) as e: 
                print("Couldn't parse", line)
    return total_cost
    
print('Total cost', portfolio_cost('Data/portfolio.csv'))
