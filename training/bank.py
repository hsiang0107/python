class Account:
    def __init__(self, name, number, balance=0):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must > 0')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('amount must > 0')
        elif amount > self.balance:
            raise RuntimeError('Balance not enough')
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance


acc = Account('Sean','1234')
print(acc.name, acc.number, acc.balance)
acc.deposit(1000)
print(acc.get_balance())

acc.withdraw(100)
print(acc.get_balance())


class CreditAccount(Account):
    def __init__(self, name, number, balance=0):
        super(CreditAccount, self).__init__(name,number,balance)
        self.creditamount=10000
        self.balance += self.creditamount

    def withdraw(self, amount):
        if amount <= self.balance + self.creditamount:
            self.balance -= amount
        else:
            raise ValueError('credit not sufficient')


acc2 = CreditAccount('Cherry', '5678')
print(acc2.name, acc2.number, acc2.balance)
acc2.deposit(1000)
print(acc2.get_balance())

acc2.withdraw(100)
print(acc2.get_balance())
