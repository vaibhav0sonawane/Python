#createw a class which contain account and 2 attributes account number and amount and make a method which shows how much amount was cradited or debited print it...
class account:
    def __init__(self,amt,acc_num):
        self.balance=amt
        self.acc=acc_num
    
    
    #amount debited
    def debit(self,amount):
        self.balance -= amount
        print("Balance amount after Debit:",self.balance)

    #amount creadited    
    def cradit(self,amount):
        self.balance += amount
        print("Balance amount after cradit:",self.balance)


acc1=account(10000,7139)
print("Your balance:",acc1.balance)
print("Your account num:",acc1.acc)

acc1.debit(200)
acc1.cradit(400)



        