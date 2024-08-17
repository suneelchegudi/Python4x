# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

a = int(input("Enter the first Number:\n"))
b = int(input("Enter the second Number:\n"))

if a > b:
    print(f"1st Number is greater than 2nd Number: {a} > {b} ")
elif a < b:
    print(f"1st Number is less than 2nd Number: {a} < {b}")
else:
    print(f"1st Number is equal to 2nd number: {a} == {b}")