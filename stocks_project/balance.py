import random
class Balance(object):
    def __init__(self):
        # balance is an integer representing cash balance
        # initializes as random value from 10000 - 25000
        self.balance = random.randint(10000, 25000)

    def credit(self, amount):
        '''Add credited amount to balance'''
        self.balance = self.balance + amount
    
    def debit(self, amount):
        '''Subtract debited amount from balance'''
        self.balance = self.balance - amount

    def get_balance(self):
        return self.balance
