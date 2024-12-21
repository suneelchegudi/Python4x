# mylist = ['First line 1\n', 'Second Line 2\n', 'Third Line 3\n']
# with open("C:\\Users\\suneel\\OneDrive\\Desktop\\Example2.txt","w") as File1:
#     File1.write("This is line 1")
# with open("C:\\Users\\suneel\\OneDrive\\Desktop\\Example2.txt","r") as File2:
#     print(File2.readline())
#
# with open("C:\\Users\\suneel\\OneDrive\\Desktop\\Example3.txt","w") as File3:
#     for line in mylist:
#         File3.writelines(line)
# with open("C:\\Users\\suneel\\OneDrive\\Desktop\\Example3.txt","a+") as File4:
#     print(File4.read())
# print("Location after read: {}".format(File4.tell()))
#
with open("C:\\Users\\suneel\\OneDrive\\Desktop\\Example3.txt","a+") as File5:
    print("location {}".format(File5.tell()))
    data = File5.read()
    if (not data):
        print("Nothing in teh file")
    else:
        print(File5.read())

    File5.seek(0,0)
    data = File5.read()
    if (not data):
        print('Read nothing')
    else:
        print(data)
    print("location after reading {}".format(File5.tell()))
