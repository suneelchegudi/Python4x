# To check if an year is a leap year
year= int(input("Enter the year to check if it is leap year: \n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a leap year")
    else:
        print(" A leap year")
else:
    print("Not leap year")