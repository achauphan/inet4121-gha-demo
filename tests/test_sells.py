#test_sells22.py
import unittest
import sys
sys.path.append('../stocks_project/')
from stocks import Stocks

class SellStockTest(unittest.TestCase):
	def test_new_portfolio(self):
		stks = Stocks()
		self.assertEqual(stks.cost_basis(), 0.0)

	def test_sell_one_company_all(self):
		stks = Stocks()
		stks.buy('HON', 10, 100.0)
		stks.sell('HON', 10)
		self.assertEqual(stks.cost_basis(), 0.0)

	def test_sell_one_company_some(self):
		stks = Stocks()
		stks.buy('HON', 10, 100.0)
		stks.sell('HON', 5)
		self.assertEqual(stks.cost_basis(), 500)

	def test_sell_one_company_none(self):
		stks = Stocks()
		stks.buy('HON', 10, 100.0)
		stks.sell('HON', 0)
		self.assertEqual(stks.cost_basis(), 1000.0)
	
# --------------------------------------------------------

	def test_sell_unowned_company(self):
		stks = Stocks()
		self.assertRaises(ValueError, stks.sell, 'A', 10)

	def test_sell_negative_amount(self):
		stks = Stocks()
		stks.buy('A', 10, 10)
		self.assertRaises(ValueError, stks.sell, 'A', -10)

	def test_company_is_not_string(self):
		stks = Stocks()
		self.assertRaises(ValueError, stks.sell, 1, 1)

	def test_sell_more_than_owned(self):
		stks = Stocks()
		stks.buy('A', 10, 100)
		self.assertRaises(ValueError, stks.sell, 'A', 1000)

	def test_sell_non_integer_inputs(self):
		stks = Stocks()
		stks.buy('A', 10, 100)
		self.assertRaises(ValueError, stks.sell, 'A', 'NaN')

