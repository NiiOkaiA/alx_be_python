class BankAccount:
    def __init__(self,account_balance):
        self.account_balance=account_balance

    def deposit(self,amount):
        self.deposit=amount
        self.account_balance+=self.deposit


    def withdraw (self,amount):
        self.withdraw=amount

        if self.withdraw<self.account_balance:
            self.account_balance-=self.withdraw
      #  else:
            

    def display_balance(self):
        print( f"Current Balance: ${self.account_balance}")







                 
