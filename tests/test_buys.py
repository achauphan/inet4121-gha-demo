#test_buys22.py
import unittest
import sys
sys.path.append('../stocks_project/')
from stocks import Stocks

class BuyStockTest(unittest.TestCase):
	def test_new_portfolio(self):
		stks = Stocks()
		self.assertEqual(stks.cost_basis(), 0.0)

	def test_buy_one_company(self):
		stks = Stocks()
		stks.buy('HON', 10, 100.0)
		self.assertEqual(stks.cost_basis(), 1000.0)

	def test_buy_two_companies(self):
		stks = Stocks()
		stks.buy('HON', 10, 100.0)
		stks.buy('GE', 10, 100.0)
		self.assertEqual(stks.cost_basis(), 2000.0)

# -------------------------------------------

	def test_buy_blank_company(self):
		stks = Stocks()
		self.assertRaises(ValueError, stks.buy, '', 10, 10)

	def test_buy_lt_0_company(self):
		stks = Stocks()
		self.assertRaises(ValueError, stks.buy, 'A', -1, 10) 
	
	def test_buy_0_company(self):
		stks = Stocks()
		self.assertRaises(ValueError, stks.buy, 'A', 0, 10)
	
	def test_buy_negative_price(self):
		stks = Stocks()
		self.assertRaises(ValueError, stks.buy, 'A', 1, -1)

	def test_company_is_not_string(self):
		stks = Stocks()
		self.assertRaises(ValueError, stks.buy, 1, 1, -1)




