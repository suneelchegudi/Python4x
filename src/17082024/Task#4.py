# - Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)
pi = 3.14
radius = float(input("Enter the radius of the circle:\n"))

def area_of_circle(radius):
    area = pi * (radius**2)
    return area

area = area_of_circle(radius)
print(f"Area of the circle is {area}")