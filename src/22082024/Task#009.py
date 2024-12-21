# Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

number = int(input("Enter the number"))

fact = 1
for num in range(1,number+1):
    fact = fact * num
print(fact)
