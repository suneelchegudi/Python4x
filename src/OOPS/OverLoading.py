import multipledispatch

class overloading:
    @multipledispatch.dispatch(int, int)
    def add(self,a,b):
        return a+b

    @multipledispatch.dispatch(int, int, int)
    def add(self,a,b,c):
        return a+b+c

    @multipledispatch.dispatch(str, str)
    def add(self,a,b):
        return a+b

obj = overloading()

print(obj.add(1,2))
print(obj.add('Suneel ', 'Chegudi'))
print(obj.add(1, 2, 3))



