class A:
    def add(self,*args):
        if args:
            sum = type(args[0])()
            print("Type is ", sum)
            for i in args:
                sum+=i
            return sum

obj = A()
print(obj.add(1,3,))
print(obj.add(1,2,3))
print(obj.add(12.3,23.4,45.6))
print(obj.add('a','c','b'))