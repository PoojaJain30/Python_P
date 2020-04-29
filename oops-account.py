#Object Oriented Programming Challenge For this challenge, create a bank account class that has two attributes:

#owner balance and two methods:

#deposit withdraw As an added requirement, withdrawals may not exceed the available balance.

#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self,name,balance):
        self.owner = name 
        self.balance = balance
        print(f'Account owner: {self.owner}')
        print(f'Account balance: ${self.balance}')
        
    def deposite(self,addbalance):
        self.addbalance = addbalance
        self.balance = self.addbalance + self.balance
        print("Deposite accepted")
        
    def withdraw(self,removebalance):
        self.removebalance = removebalance
        print(self.removebalance)
        if (self.removebalance <= self.balance):
            self.balance = self.balance - self.removebalance
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")
       
a = Account('poo',100)
a.owner
a.deposite(50)
a.withdraw(20)

#other approch
class Account1:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
        
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')