file = open("suneel.txt",'a')
file.write("Lane number 3")
file1 = open("suneel.txt",'r')
content = file1.readlines()
for line in content:
    print(line, end = "\n")