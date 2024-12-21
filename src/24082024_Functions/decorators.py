def my_decorator(func):
    def wrapper():
        print("Decorator#1")
        func()
    return wrapper

@my_decorator
def call_myfunc():
    print("Here you go ")

call_myfunc()

o = lambda total: total**3
print(o(10))