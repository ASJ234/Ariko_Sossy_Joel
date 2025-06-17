#A simple bank account system of deposits, withdrawals, and account information

class BankAccount:  
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        print("Balance: ",self.balance)

    def get_account_number(self):
        print("Account Number: ",self.account_number) 
        
    def get_account_holder(self):
        print("Account Holder: ",self.account_holder)
        
        
      
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.01):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate
    
    def get_interest_rate(self):
        return self.interest_rate
    
    def get_account_type(self):
        return "Savings Account"
    
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=1000):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def get_overdraft_limit(self):
        return self.overdraft_limit
    
    def get_account_type(self):
        return "Current Account"

    
# Instantiate accounts
savings_account = SavingsAccount("1234567890", "John Doe", 1000, 0.05)
current_account = CurrentAccount("0987654321", "Jane Smith", 2000, 1000)

# Infinite loop for bank operations
while True:
    print("\n================ BANK MENU ================\n")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Balance")
    print("4. View Account Information")
    print("5. Calculate Interest (Savings Only)")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("Thank you for using the bank system. Goodbye!")
        break

    # Choose account
    acc_type = input("Select account type (savings/current): ").lower()
    if acc_type == "savings":
        account = savings_account
    elif acc_type == "current":
        account = current_account
    else:
        print("Invalid account type.")
        continue

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == '3':
        account.get_balance()

    elif choice == '4':
        print("--------------------------------------------------")
        print(f"Account Type: {account.get_account_type()}")
        account.get_account_holder()
        account.get_account_number()
        account.get_balance()
        if isinstance(account, SavingsAccount):
            print(f"Interest Rate: {account.get_interest_rate()}")
        elif isinstance(account, CurrentAccount):
            print(f"Overdraft Limit: {account.get_overdraft_limit()}")
        print("--------------------------------------------------")

    elif choice == '5':
        if isinstance(account, SavingsAccount):
            interest = account.calculate_interest()
            print(f"Calculated Interest: {interest}")
        else:
            print("Interest calculation is only available for savings accounts.")

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
