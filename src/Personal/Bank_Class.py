class Bankclass:
    def __init__(self,ac_number,ac_name,ac_ifsccode,ac_balance):
        self.bank_account_number = ac_number
        self.bank_account_name = ac_name
        self.bank_ifsccode = ac_ifsccode
        self.bank_balance = ac_balance
    def show_balance(self):
        print(self.bank_balance)
    def deposit(self,amount):
        self.bank_balance += amount

    def withdraw(self,amount):
        self.bank_balance -= amount

    def display(self):
        print(self.bank_account_number,self.bank_account_name,self.bank_ifsccode,self.bank_balance, sep=" - ")

object1 = Bankclass(123456,"Suneel", "SBIN00001", 1000)
# object1.display()

object1.deposit(20000)
object1.show_balance()
object1.withdraw(10000)
object1.show_balance()

