# - Explain the difference between the = operator and the == operator in Python.

#  = Operator is used to assign values to the variable
age = 65
print(f"'=' Operator :{age}")

# == Operator is used for comparison
a = 2
b = 3
print(f"'==' Operator returns False as 'a' is not equal to 'b': {a==b}")
x = 5
y = 5
print(f"'==' Operator returns True as 'x' is not equal to 'y': {x==y}")

# - What does the ** operator do in Python, and how is it used?
# ** Operator is used as exponentiation
print(f"'**' Exponentiation - a to the power of b is : {a**b}")

# - What does the ^ operator do in Python, and in what context is it commonly used?
# used as Bitwise XOR - This operation compares each bit of the first operand to the corresponding bit of the second operand.
print(f"Bitwise XOR of a and b is : {a^b}")

i = True
j = False
print(i ^ j)
