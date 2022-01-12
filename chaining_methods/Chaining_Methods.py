class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_deposit(self,amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print((f"User:{self.name}, Balance: ${self.balance}"))
        return self

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return self

Ed = User("Ed", 150)
Edd = User("Edd",20)
Eddy = User("Eddy" , 0)

Ed.make_deposit(10).make_deposit(20).make_deposit(20).make_withdrawal(100).display_user_balance()

Edd.make_deposit(40).make_deposit(10).make_withdrawal(60).display_user_balance()

Eddy.make_deposit(100).make_withdrawal(40).make_withdrawal(40).make_withdrawal(40).display_user_balance()

Ed.transfer_money(Eddy,20).display_user_balance()

Eddy.display_user_balance()