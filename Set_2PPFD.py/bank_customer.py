class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid amount for deposit.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
    
    def add_account(self, account_number, customer):
        if account_number not in self.accounts:
            self.accounts[account_number] = {'customer': customer, 'account': Account(account_number)}
            print(f"Account {account_number} created for customer {customer.name}.")
        else:
            print(f"Account {account_number} already exists.")
    
    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]['account']
        else:
            print("Account not found.")
            return None

# Example usage:
customer1 = Customer("Alice", "123 Main St")
bank = Bank("MyBank")
bank.add_account("220101", customer1)
account = bank.get_account("220101")
account.deposit(1000)
account.withdraw(500)
