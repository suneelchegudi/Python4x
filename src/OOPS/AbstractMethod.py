from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print('this is concrete method')
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("Method1 implemented in subclass")

    def method3(self):
        print("Method3 impletemented in subclass")

obj1 = B()
obj1.method1()
obj1.method2()
obj1.method3()