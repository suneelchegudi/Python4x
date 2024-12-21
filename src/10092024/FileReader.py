import os
folder_path = "D:\Python4x\src\10092024\suneel"
full_path = os.path.join(r"D:\Python4x\src\10092024\suneel", "suneel.txt")

file = open(full_path, 'r')
content = file.read()
print (content)
