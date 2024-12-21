import io
import os

filepath = os.getcwd()
print(os.name)
print("Current path is ", filepath)
print(os.listdir())
for file in os.listdir('.'):
    print(file)
