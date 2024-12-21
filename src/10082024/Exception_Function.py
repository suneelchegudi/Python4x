def division(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        print("Warning**:Denominator should not be Zero")
        return None
    except ValueError:
        print("Warning**: Should be a Numeric")
        return None
    finally:
        print("Printed Successfully")


a = int(input("Enter Numerator:"))
b = int(input("Enter Denominator"))

print(division(a,b))