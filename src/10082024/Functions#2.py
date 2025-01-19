def sum_of_three(a=10, b = 15, c = 15):
    return a+b+c

result = sum_of_three(a=50,b=20)
print(result)

def pizza_making(*toppings, base):
    print(toppings,base)

pizza_making("chicken", "cheese", "salad", base= "thin crust")

def pizza_making(toppings, *base):
    print(toppings,base)

pizza_making("thin crust", "chicken", "cheese", "salad")