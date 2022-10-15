#test_stocks2.py

import unittest
from stocks1 import Stocks

class StocksTest(unittest.TestCase):
	def test_buy_one_company(self):
		stks = Stocks()
		stks.buy('Hon', 100, 132.0)
		self.assertEqual(stks.cost_basis(), 13200.0)
	
	def test_sell_one_company(self):
		stks = Stocks()
		stks.buy('Hon', 10, 10)
		stks.sell('Hon', 1)
		self.assertEqual(stks.cost_basis(), 90)

	def test_sell_extra_company(self):
		stks = Stocks()
		stks.buy('Hon', 10, 10)
		#stks.sell('Hon', 100)
		self.assertEqual(stks.sell('Hon', 100), 'Error: attempting to sell more shares than owned')

	def test_sell_unknown_company(self):
		stks = Stocks()
		self.assertEqual(stks.sell('Hon', 1), 'Error: stock not in portfolio')


if __name__ == '__main__':
        unittest.main()
