import csv
with open("testdata.csv",'r') as file:
    reader = csv.reader(file)
    for col in reader:
        print(col[0],col[1], sep="|")