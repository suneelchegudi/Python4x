class ParentClass:
    __parentData = 50

    def parentMethod(self):
        print(self.__parentData)

class ChildClass(ParentClass):
    def childMethod(self):
        print(self.__parentData)


obj1 = ParentClass()
obj1.parentMethod()
# print(obj1.parentData)
obj2 = ChildClass()
obj2.childMethod()
# print(obj2.parentData)
