# Zero division error
# print(10/0)

# Type error
# print(1+"1")

# /index error
# list  = [1,2,3]
# print(list[4])
try:

    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = a/b
    print("Result is ", c)
except Exception as e:
    print(e)
    print("Please check your inputs")
print (" End of the program")