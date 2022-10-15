# stocks1.py is a simple application to motivate unit testing.
# stock trading application has an in mem rep of stocks acquired
# represented as a list of lists where each element is a purchased stock

class Stocks(object):
    """An in mem stock portfolio"""

    def __init__(self):
        # stocks is a list of lists where each element
        # is a list of company name, num shares purchased
        # and the price per share
        self.stocks = []

    def buy(self, company, num_shares, unit_price):
        """Buy `num_shares` in 'company' at `unit_price` per share"""
        self.stocks.append([company, num_shares, unit_price])

    def cost_basis(self):
        """Calculate the cost basis for the stocks acquired"""
        basis = 0.0
        for company, shares, unit_price in self.stocks:
            basis += shares * unit_price
        return basis

    def cost_basis_company(self, company):
        pass

    def sell(self, company, num_shares):
        """
        Sells stocks in portfolio if possible
    	>>> s=Stocks()
		>>> s.buy('c', 10, 10)
		>>> s.cost_basis()
		100.0
		>>> s.sell('c', 1)
		>>> s.cost_basis()
		90.0
		>>> s.sell('c', 100)
		'Error: attempting to sell more shares than owned'
		>>> s.sell('a', 1)
		'Error: stock not in portfolio'
		>>> s.sell('c', 9)
		>>> s.print_portfolio()
		Company, Number Shares, Share Price
		"""
        # stk is a list containing company name, num_shares, unit price
        for stk in self.stocks:
            # check if company is in portfolio
            if stk[0] == company:
                # check number of shares able to be sold
                if num_shares <= stk[1]:
                    stk[1]= stk[1] - num_shares
                    if stk[1] == 0:
                        self.stocks.remove(stk)
                    return
                else:
                    return "Error: attempting to sell more shares than owned"
        return "Error: stock not in portfolio"

    def print_portfolio(self):
        print('Company,', 'Number Shares,', 'Share Price')
        for company, num_shares, unit_price in self.stocks:
            print(company, num_shares, unit_price)
