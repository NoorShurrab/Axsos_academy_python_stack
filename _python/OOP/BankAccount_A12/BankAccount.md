# Bank Account Class Documentation
The BankAccount class represents a simplified bank account system that handles interest rates, balance management, and supports Method Chaining.

### Attribute
1. int_rate : default is 0.01
2. balance : default is 0

### Methods
1. __init__(self, int_rate=0.01, balance=0) 
    - initializes a new bank account with a specific interest rate and an initial balance.

2. deposit(self, amount)
    - Increases the account balance by the given amount.
    - Returns self to enable method chaining.

3. withdraw(self, amount)
    - Decreases the account balance by the given amount if funds are sufficient.
    - If there is not enough money, it prints "Insufficient funds" and charges a $5 fee.
    - Returns self to enable method chaining.

4. display_account_info(self)
    - Prints the current balance of the account.
    - Returns self to enable method chaining.

5. yield_interest(self)
    - Increases the account balance by (balance * interest rate), provided the balance is positive.
    - Returns self to enable method chaining.
