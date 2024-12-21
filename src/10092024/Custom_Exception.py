class Custom_Exception(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(message)

balance = 100
withdraw = int(input("Enter the amount to withdraw"))

if withdraw > balance:
    raise Custom_Exception("Balance is low")
else:
    print("Total Balance is ", (balance-withdraw))


