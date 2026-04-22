# User Class Documentation
The User class represents a bank account holder in the system

### Attributes
1. name
2. phone
3. balance

### Methods
1.  __init__(self, name, phone, balance=0) → Initializes a new user with a name, phone number, and an default starting balance

2. display_user_balance(self) → Displays the user's name along with their current balance.

3. make_deposit(self, amount)
    - Adds the specified amount to the user's balance.

4. make_withdrawal(self, amount)
    - Deducts the specified amount from the user's balance.

5. transfer_money(self, other_user, amount) → Transfers a specified amount from the current user to another user.
This method:
    - Withdraws the amount from the current user
