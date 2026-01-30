class createAccount:
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc
    
    def debit(self,amount):
        self.bal-=amount
        print(amount," was debited from account : ",self.acc)
    
    def credit(self,amount):
        self.bal+=amount
        print(amount," was credited to account : ",self.acc)
    

    def balance(self):
        print("current balance is : ",self.bal)


account1=createAccount(10000,1234)

account1.debit(100)
account1.credit(2000)
account1.balance()