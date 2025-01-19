class ParentClass:
    _parentData = 10
    def parentMethod(self):
        print(self._parentData)

    @property
    def parentData(self):
        return self._parentData


class ChildClass(ParentClass):
    def childMethod(self):
        print(self._parentData)

obj1 = ParentClass()
obj1.parentMethod()
print(obj1._parentData)
obj2 = ChildClass()
obj2.childMethod()
print(obj2._parentData)
