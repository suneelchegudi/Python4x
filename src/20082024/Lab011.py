num1 = int(input("Enter the number#1\n"))
num2 = int(input("Enter the number#2\n"))
num3 = int(input("Enter the number#3\n"))

print(f"Maximum of num1 and num2 is {max(num1,num2,num3)}")

if num1 > num2 and num1 > num3:
    print(f"Number#1 {num1} is greater than {num2} and {num3}")
elif num2 > num1 and num2 > num3:
    print(f"Number#2 {num2} is greater than {num1} and {num3}")
elif num3 > num1 and num3 > num1:
    print(f"Number#3 {num3} is greater than {num1} and {num2}")