import math

def sqrtofthenumber(number1):
    try:
        result = math.sqrt(number1)
        print(f"result is {result}")
    except ValueError:
        print("Enter Positive Value")

number1 =float(input("Enter value"))
sqrtofthenumber(number1)
