class employees():
    name = None
    age= None
    phone = None
    address = None
    eid = None
    def __init__(self,name, age, phone, address, eid):
        print("WElcome to the world of my business")
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid
        print(self.name)
        print(self.age)
        print(self.phone)
        print(self.address)
        print(self.eid)
    # def employess2(self):
        #print("Total Number of employees are 1000, including ", self.name)

name = input("Enter name of the employee")
sage = input("Enter age of the employee")
phone = input("Enter phone")
address = input("Enter address")
eid = input("Enter Employee ID")

mb = employees(name,age,phone,address,eid)

