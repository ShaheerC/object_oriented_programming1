class BankAccount:

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
    
    def __str__(self):
        return "BANKACCOUNT: balance: {} - interest_rate: {}".format(self.balance, self.interest_rate)

    def deposit(self, num):
        self.balance += num

    def withdraw(self, number):
        self.balance -= number
    
    def gain_interest(self, gain_int):
        self.balance *= gain_int

td = BankAccount(1000, 10)
print(td.balance)
print(td.interest_rate)
print(td)
td.deposit(200)
print(td)
td.withdraw(200)
print(td)
td.gain_interest(1.1)
print(td)
