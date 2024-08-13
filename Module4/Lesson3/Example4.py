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
    def get_account_holder(self):
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


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance, interest_rate):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    # Method to add interest to the balance
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest {interest} added to the balance.")

    # Overriding the withdraw method to include a withdrawal limit
    def withdraw(self, amount):
        if amount >500:
            print("Withdrawal limit exceeded.")
        else:
            super().withdraw(amount)

class CheckingAccount(BankAccount):
    def __init__(self,account_holder, initial_balance, transaction_fee):
        super().__init__(account_holder, initial_balance)
        self.transaction_fee = transaction_fee

    # Overriding the withdraw method to include a transaction fee
    def withdraw(self, amount):
        total_amount = amount + self.transaction_fee
        if total_amount <= self.get_balance():
            self.set_balance(self.get_balance() - total_amount)
            print(f"Withdrawn: {amount}, Transaction Fee: {self.transaction_fee}")
        else:
            print("Insufficient balance for withdrawal and transaction fee.")

# Creating instances of the subclasses
savings = SavingsAccount("Alice", 1500, 0.05)
checking = CheckingAccount("Bob", 2000, 20)

# Savings account usage
savings.add_interest()  # Adds interest to the balance
savings.withdraw(200)   # Withdraws money within limit
print(f"Savings Account Balance: {savings.get_balance()}")

# Checking account usage
checking.deposit(500)   # Deposits money into account
checking.withdraw(300)  # Withdraws money, including the transaction fee
print(f"Checking Account Balance: {checking.get_balance()}")

# Updating account holders
savings.set_account_holder("Alice Smith")
checking.set_account_holder("Bob Johnson")