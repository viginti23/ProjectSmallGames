class Wallet:
    def __init__(self, money=0):
        self.money = money

    def __str__(self):
        return self.money

    def __repr__(self):
        return self.money
