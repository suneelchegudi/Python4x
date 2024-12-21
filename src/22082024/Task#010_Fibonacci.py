# Fibonacci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

# num = int(input("Enter the number "))

# # i | sum + i | sum
# # 0 |  0 + 0  | 0
# # 1 |  0 + 1  | 1
# # 2 |  1 + 2  | 3
# # 3 |  3 + 3  |
#
# sum = 0
# f1 = 0
# f2 = 1
# print (f1 , f2)
# sum = f1+f2
# while (sum < num):
#     print(f"{sum}")
#     f1 = f2
#     f2 = sum

num = int(input("Enter a number to create Fibonacci series : \n"))
series = []
a, b = 0, 1
for i in range(num + 1):
    series.append(a)
    a = b
    b = a + b

print(f"Fibonacci series for number {num} is {series}")

# n = 10
# num1 = 0
# num2 = 1
# next_number = num2
# count = 0
#
# while count <= n:
#     print(next_number, end=" ")
#     count += 1
#     num1, num2 = num2, next_number
#     next_number = num1 + num2
# print()