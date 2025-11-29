class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        result = self.account_balance + amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            return True
        else:
            return False
        
        #result = self.account_balance - amount


    def display_balance(self):
        print(f"Your Current account Balance is :{self.account_balance}")
    
    