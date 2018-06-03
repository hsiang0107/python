class Account:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


Seanacc = Account('123-456-789', 'Sean')
print(Seanacc.number, Seanacc.name, Seanacc.balance)
Seanacc.deposit(1000)
print(Seanacc.balance)
Seanacc.withdraw(300)
print(Seanacc.balance)