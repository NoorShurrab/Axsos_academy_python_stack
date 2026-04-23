# Implements OOP principles by associating the User class with a BankAccount class.
# It manages user data through external module imports and handles financial 
# operations—like deposits, withdrawals, and transfers—by interacting with 
# the BankAccount instance stored within each User.
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BankAccount_A12.BankAccount import AccountBank
class User:
    def __init__(self, name, phone, balance = 0):
        self.name = name
        self.phone = phone
        self.account = AccountBank(int_rate = 0.01, balance = balance)
        print(f"User is created with name: {self.name}, phone: {self.phone}, balance: {self.account.balance}$")

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}$")
    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

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
