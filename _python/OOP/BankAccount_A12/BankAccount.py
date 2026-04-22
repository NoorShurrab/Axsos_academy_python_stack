# Create a BankAccount class with interest rate and balance attributes, implements deposit, withdraw, and yield_interest methods with method chaining support.
class AccountBank:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        print(f"Account is created with interest rate: {self.int_rate}, balance: {self.balance}$")

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}$")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
account_one = AccountBank(0.03, 2000)
account_two = AccountBank(0.06, 3000)

account_one.deposit(400).deposit(100).deposit(700).withdraw(300).yield_interest().display_account_info()
account_two.deposit(2000).deposit(400).withdraw(100).withdraw(100).withdraw(200).withdraw(100).yield_interest().display_account_info()
