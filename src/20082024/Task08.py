side1 = float(input("Enter the length of side#1:\n"))
side2 = float(input("Enter the length of side#2:\n"))
side3 = float(input("Enter the length of side#3:\n"))

if side1 == side2 and side2 == side3 and side1 == side3:
    print ("Equilateral Triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("isosceles")
else:
    print("Scalen")


