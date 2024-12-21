try:
    with open("sunee.txt", 'r') as file:
        content = file.readlines()
        print(content)
except FileNotFoundError as fnfe:
    print("File Not Found:", fnfe)
finally:
    try:
        file.close()
    except NameError as ne:
        print("name Error:", ne)
