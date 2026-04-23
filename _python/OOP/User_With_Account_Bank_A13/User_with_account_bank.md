# User Class Documentation
The User class represents a bank account holder and acts to manage their financial activities through an associated bank account

### Attributes
1. name
2. phone
3. account: (Instance) An association with the AccountBank class, which handles the actual financial logic.

### Methods
1. __init__(self, name, phone, balance=0)
    - Initializes a new user and creates an associated bank account instance.

2. display_user_balance(self)
    - Displays the user's name and their current balance by accessing the associated account instance.

3. make_deposit(self, amount) → Deposits a specified amount into the user's associated bank account.
    - Mechanism: Calls the deposit() method from the AccountBank class.

4. make_withdrawal(self, amount) → Deducts a specified amount from the user's associated bank account.
    - Mechanism: Calls the withdraw() method from the AccountBank class.

5. transfer_money(self, other_user, amount) → Transfers a specified amount from the current user to another user.
    - Withdraws the amount from the current user's account using self.make_withdrawal().
    - Deposits the same amount into the other_user's account using other_user.make_deposit().
