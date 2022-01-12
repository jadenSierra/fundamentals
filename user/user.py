class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_deposit(self,amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        return print((f"User:{self.name}, Balance: ${self.balance}"))

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount

Ed = User("Ed", 150)
Edd = User("Edd",20)
Eddy = User("Eddy" , 0)

Ed.make_deposit(10)
Ed.make_deposit(20)
Ed.make_deposit(20)
Ed.make_withdrawal(100)

Edd.make_deposit(40)
Edd.make_deposit(10)
Edd.make_withdrawal(60)

Eddy.make_deposit(100)
Eddy.make_withdrawal(40)
Eddy.make_withdrawal(40)
Eddy.make_withdrawal(40)

Ed.display_user_balance()
Edd.display_user_balance()
Eddy.display_user_balance()

Ed.transfer_money(Eddy,20)
Ed.display_user_balance()
Eddy.display_user_balance()