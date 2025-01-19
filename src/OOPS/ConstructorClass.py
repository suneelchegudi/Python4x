class BankAccount1():
    def __init__(self,accountNo,accountName,ifscCode,balance):
        self.accountNo = accountNo
        self.accountName = accountName
        self.ifscCode = ifscCode
        self.balance = balance

    def Deposit(self,depositAmount):
        self.balance = self.balance + depositAmount
        print(self.balance)
    def Withdraw(self,withdrawAmount):
        self.balance = self.balance - withdrawAmount
        print(self.balance)
    def CheckBalance(self):
        print(self.balance)
    def displayAccountDetails(self):
        print(self.accountNo,self.accountName,self.ifscCode,self.balance, sep='--')

obj1 = BankAccount1(12354,'Suneel','BOFA1234',10000)
# obj1.displayAccountDetails()
obj1.CheckBalance()
obj1.Deposit(10000)
obj1.Withdraw(5000)
obj1.CheckBalance()