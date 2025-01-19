class BankAccount:
    AccountNumber = 123
    AccountName = 'Suneel'
    balance = 1000
    def deposit(self,amount):
        balance = balance + amount
        print(balance)

obj1 = BankAccount()
obj1.deposit(1000)
print(BankAccount.AccountNumber)

