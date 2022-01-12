class BankAccount:

    def __init__(self,int_rate=0.02,balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        elif self.balance < amount:
            print( "Insufficient funds: Charging a $5 fee")
            self.balance -= (amount + 5)
        return self
    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate
        return self

Tom = BankAccount(int_rate=0.8,balance=100)
Jerry = BankAccount(balance=500)

Tom.deposit(25).deposit(25).deposit(25).withdraw(100).yield_interest().display_account_info()
Jerry.deposit(100).deposit(100).withdraw(20).withdraw(10).withdraw(30).withdraw(5).yield_interest().display_account_info()