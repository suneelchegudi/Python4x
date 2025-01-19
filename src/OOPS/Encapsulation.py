class Parent:
    publicData = 10
    def publicMethod(self):
        print(self.publicData)
class Child(Parent):
    def childMethod(self):
        print(self.publicData)

class grandChild():
    def grandChildMethod(self):
        

obj1 = Parent()
obj1.publicMethod()
print(obj1.publicData)

chd1 = Child()
chd1.childMethod()
print(chd1.publicData)

gchild = grandChild()
