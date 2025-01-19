def safety_rules(func):
    def wrapper():
        print("Before driving")
        func()
        print("After Driving")
    return wrapper()
@safety_rules
def driving_bike():
    print("Driving started....")

