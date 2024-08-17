# Develop a Python script that calculates the square and cube of a given number.

# Get the number from user
num = int(input("Enter the number: \n"))

print("Square of the", num, "is", num**2)
print("Cube of the", num, "is", num**3)

# Alternatively we can use Pow function

print("Square of the", num, "using pow function is", pow(num,2))
print("Square of the", num, "using pow function is", pow(num,3))