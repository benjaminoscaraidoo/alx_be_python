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
        #acc_bal = {self.account_balance}
        #float_set = set(map(float, self.account_balance))
        #print(f" Current Balance: tpye is  {type(acc_bal)}")
        print(f" Current Balance: ${self.account_balance}.00")
        #print(f" Current Balance: ${self.account_balance}")
    