
from Ch05.sub1.Account import  Account

class StockAccount(Account):

    def __init__(self, bank, id, name, money, stock, price, amount):
        Account.__init__(self, bank, id, name, money)
        self.stock = stock
        self.price = price
        self.amount = amount

    def sell(self, price, amount):
        self.amount -= amount
        self.money += (price * amount)
    def buy(self, price, amount):
        self.amount += amount
        self.money -= (price / amount)
    def show(self):
        Account.show(self)
        print('종목 : ', self.stock)
        print('수량 : ', self.amount)
        print('가격 : ', self.price)