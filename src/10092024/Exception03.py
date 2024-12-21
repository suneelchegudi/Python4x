try:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = a/b
except ValueError as ve:
    print("Value Error, you have entered teh string instead of integer")
except ZeroDivisionError as ze:
    print("Number two should Not be zero")
else:
    print("Result is ", c)
finally:
    print("This code is perfect")