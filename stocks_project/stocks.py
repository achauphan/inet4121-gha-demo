from balance import *

class Stocks(object):
    """An in mem stock portfolio"""

    def __init__(self):
        # xacts is a list of lists where each element
        # is a list of company name, num shares purchased
        # and the price per share
        self.xacts = []
        self.balance = Balance()

    def buy(self, company, num_shares, unit_price):
        """Buy `num_shares` in 'company' at `unit_price` per share"""
        if not isinstance(company, str) or len(company) == 0 or num_shares <= 0 or unit_price <= 0:
            raise ValueError('Invalid parameters')

        total_cost = num_shares * unit_price
        if total_cost < self.balance.get_balance():
            self.balance.debit(total_cost)
            self.xacts.append([company, num_shares, unit_price])
        else:
            raise ValueError('Insufficient funds for requested purchase')

    def cost_basis(self):
        """Calculate the cost basis for the stocks acquired"""
        basis = 0.0
        for company, shares, unit_price in self.xacts:
            basis += shares * unit_price
        return basis

    def cost_basis_company(self, company):
        basis = 0.0
        for comp, shar, unit in self.xacts:
            if comp == company:
                basis += shar * unit
        return basis

    def sell(self, company, num_shares):
        for stock in self.xacts:
            if stock[0] == company:
                if stock[1] < num_shares:
                    raise ValueError('Insufficient shares for requested sale')
                stock[1] -= num_shares
                sell_price = num_shares * stock[2]
                self.balance.credit(sell_price)
                if stock[1] == 0:
                    self.xacts.remove(stock)
                return
        raise ValueError('No matching company found in portfolio')


    def print_portfolio(self):
        print('Company,', 'Number Shares,', 'Share Price')
        for company, num_shares, unit_price in self.xacts:
            print(company, num_shares, unit_price)
