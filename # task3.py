# task3.py

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds for withdrawal.")

    def display_balance(self):
        print(f"Account balance: ${self.balance}")

# Create an account and perform transactions
account = BankAccount("123456789", "John Doe", 500)
account.deposit(200)
account.withdraw(100)
account.display_balance()