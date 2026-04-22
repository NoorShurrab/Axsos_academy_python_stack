# implements OOP principles to simulate a banking system, allowing for the creation of users 
# and managing balances via deposit, withdrawal, and inter-user transfer methods.
class User:
    def __init__(self, name, phone, balance = 0):
        self.name = name
        self.phone = phone
        self.balance = balance
        print(f"User is created with name: {self.name}, phone: {self.phone}, balance: {self.balance}$")

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}$")
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self


noor = User("Noor","059567112", 1000)
heba = User("Heba","059567113", 0)
rana = User("Rana","059567114", 500)

#Each method returns 'self' to enable Method Chaining, allowing multiple operations to be called in a single line.
noor.make_deposit(200).make_deposit(100).make_deposit(600).make_withdrawal(300).display_user_balance()

heba.make_deposit(700).make_deposit(400).make_withdrawal(100).make_withdrawal(300).display_user_balance()

rana.make_deposit(1000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

noor.transfer_money(heba, 200)
noor.display_user_balance()
heba.display_user_balance()