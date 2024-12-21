a= 1
try:
    b = int(input("Enter b value: "))
    a = a/b
except ZeroDivisionError:
    print("Cant be zero")
except ValueError:
    print("Should be a numeric")
except:
    print("unknown error")
else:
    print("Success a is :", a)