class BankAccount:
    def __init__(self, ac_number,ac_name,ifsc_code,ac_balance):
        self.bank_ac_number = ac_number
        self.bank_ac_name = ac_name
        self.bank_ifsc_code = ifsc_code
        self.bank_ac_balance = ac_balance
        # print(self.bank_ac_number,self.bank_ac_name,self.bank_ifsc_code,self.bank_ac_balance)
    def check_balance(self):
        print(self.bank_ac_balance)
    def withdraw(self,amount):
        self.bank_ac_balance -= amount

    def deposit(self,amount):
        self.bank_ac_balance += amount


object1 = BankAccount(1234566789,"Suneel","SBIN001",10000)
object1.check_balance()
object1.deposit(5000)
object1.check_balance()
object1.withdraw(2000)
object1.check_balance()