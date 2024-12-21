# Tuples
A = (0, 1, 2, 3)
print(A[-1])

# Dictionaries
D = {'a':0,'b':1,'c':2}
a = D.values()
print(a)

# List
L = ['x','y','z']
print(L)
print(len(L))
L.append(['a','b'])
print(L)
print(len(L))


for number in range(10, 0, -2):
    print(number)

i = 0

while i <= 5:
    print(i)
    i = i +1

while i < 5:
    print(i)
    i = i +1

print(3 + 2 * 2)

# Sets *****************
album_list1 = ["D", "A", "S", "J"]
album_list2 = ["X", "A", "S", "Y"]
album_list1 = set(album_list1)
album_list2 = set(album_list2)
intersection = album_list1 & album_list2
print(intersection)

