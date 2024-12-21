import os

try:
    file = open('text.txt','r')
    print(file.read())
except FileNotFoundError as fe:
    print("File not found, fix the path or create an error")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)