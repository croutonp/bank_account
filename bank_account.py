class BankAccount:
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = amount + self.balance
        
        print(f"you have deposited {amount} and your balance is now {self.balance}")
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5            
        else:
            self.balance -= amount
            print(f"you've withdrawn {amount} your new balance is {self.balance - amount}")
        return self    
    
    def display_account_info(self):
        print(f"your balance is {self.balance}")
    
    def yield_interest(self):
        self.balance *= 1 + self.int_rate 
        print(f"your yield is {self.int_rate} and your balance is {self.balance}")
        return self

christian = BankAccount(.01, 20)
monica = BankAccount(.02, 50)

monica.deposit(20).deposit(20).deposit(20).withdraw(1).yield_interest()