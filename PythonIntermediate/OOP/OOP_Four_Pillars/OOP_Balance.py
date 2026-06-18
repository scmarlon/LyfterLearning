class BankAccount():
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. Current balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawal successful. Current balance: {self.balance}")
    

class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        super().__init__()
        self.min_balance = min_balance
    
    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print("The minimum balance requirement is not met. Withdrawal failed.")
        else:
            super().withdraw(amount)

# Example usage:
savings_account = SavingsAccount(min_balance=100)
savings_account.deposit(150)  # Deposit successful. Current balance: 150
savings_account.withdraw(30)   # Withdrawal successful. Current balance: 120
savings_account.withdraw(50)   # The minimum balance requirement is not met. Withdrawal failed.