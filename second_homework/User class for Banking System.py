#https://www.codewars.com/kata/user-class-for-banking-system/train/python
class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, money):
        if self.balance < money:
            raise ValueError
        self.balance -= money
        return self.name + ' has ' + self.balance

    def check(self, other_user, money):
        if other_user.checking_account == False or other_user.balance < money:
            raise ValueError
        self.balance += money
        other_user.withdraw(money)
        return self.name + ' has ' + self.balance + ' and ' + other_user + ' has ' + other_user.balance

    def add_cash(self, money, balance):
        self.balance += money
        return self.name + ' has ' + self.balance + ' . '