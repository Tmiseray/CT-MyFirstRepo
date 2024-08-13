"""
Example: Encapsulation in a BankAccount Class

Let's create a BankAccount class to use getters and setters for both public and private attributes. This approach will showcase how we can manage and protect the state of our objects, ensuring a robust and secure implementation. We'll also add a few additional features to our class to make it more realistic and functional.

Objective: 
Implement a BankAccount class with a private balance and public account holder name. Use getters and setters to interact with these attributes and include methods for depositing and withdrawing funds.

The balance is a private attribute with a private setter, ensuring that the balance can only be modified through the deposit and withdrawal methods. The account holder's name is a public attribute, but we provide a getter and setter for it, following the encapsualtion principle. This design maintains the integrity of the BankAccount class by controlling how its attributes are accessed and modified, akin to how a real bank account operates.

"""

class BankAccount:
    def __init__(self, account_holder, initial_balance = 0):
        self.__balance = initial_balance    # Private attribute for balance
        self.account_holder = account_holder    # Public attribute for account holder

    # Getter for balance
    def get_balance(self):
        return self.__balance
    
    # Setter for balance - Private as balance should not be directly set
    def set_balance(self, new_balance):
        self.__balance = new_balance

    # Getter for account holder
    def get_account_holder(self,):
        return self.account_holder

    # Setter for account holder
    def set_account_holder(self, new_holder):
        self.account_holder = new_holder

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    # Withdrawal method
    def withdraw(self, amount):
        if 0 < amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

# Example usage
account = BankAccount("Alex", 1000)
print(f"Account Holder: {account.get_account_holder()}")
print(f"Initial Balance: {account.get_balance()}")

account.deposit(500)
account.withdraw(200)
print(f"Updated Balance: {account.get_balance()}")

account.set_account_holder("Charlie")
print(f"New Account Holder: {account.get_account_holder()}")