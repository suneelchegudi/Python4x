class A:
    __a = 10
    ___b = 20
    ____c = 30
    _____d = 40
    __e_ = 50
    __f__ = 60
    ___g___ = 80
    ___h_ = 90
    _i_ = 100
    ___j___ = 200

    def getPrivateDate(self):
        print(self.__a)

class B(A):
    def getPrivateMember(self):
        print(self._A__a)

ob1 = A()
ob1.getPrivateDate()
print(ob1._A__a)

obj2 = B()
obj2.getPrivateMember()
print(obj2._A__a)
