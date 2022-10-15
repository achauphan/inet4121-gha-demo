# teststocks1.py
from stocks1 import Stocks

my_stocks = Stocks()
print( 'Initial cost basis is {}'.format( my_stocks.cost_basis() ) )

my_stocks.buy('hon',100, 128.)
print( 'Portfolio cost basis is {}'.format( my_stocks.cost_basis() ) )
my_stocks.buy('hon',50, 128.)
print( 'Portfolio cost basis is {}'.format( my_stocks.cost_basis() ) )
my_stocks.buy('ge', 50, 235.5)
print( 'Portfolio cost basis is {}'.format( my_stocks.cost_basis() ) )

my_stocks.print_portfolio()
