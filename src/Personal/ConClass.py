class Constructor_Class:
    def __init__(self):
        print("This is method is automatically called in the init classmethod")
    def class_method(self):
        print("this is class method is called externally using object")


obj1 = Constructor_Class()
obj1.class_method()