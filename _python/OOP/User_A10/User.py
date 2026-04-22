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
    def make_withdrawal(self, amount):
        self.balance -= amount

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)


noor = User("Noor","059567112", 1000)
heba = User("Heba","059567113", 0)
rana = User("Rana","059567114", 500)

noor.make_deposit(200)
noor.make_deposit(100)
noor.make_deposit(600)
noor.make_withdrawal(300)
noor.display_user_balance()

heba.make_deposit(700)
heba.make_deposit(400)
heba.make_withdrawal(100)
heba.make_withdrawal(300)
heba.display_user_balance()

rana.make_deposit(1000)
rana.make_withdrawal(100)
rana.make_withdrawal(100)
rana.make_withdrawal(100)
rana.display_user_balance()

noor.transfer_money(heba, 200)
noor.display_user_balance()
heba.display_user_balance()