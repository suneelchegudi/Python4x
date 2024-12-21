from random import randint as rnd
memReg = 'C:\\Users\\suneel\\OneDrive\\Desktop\\members1.txt'
exReg = 'C:\\Users\\suneel\\OneDrive\\Desktop\\inactive1.txt'
fee =('yes','no')

def genFile(curFile,oldFile):
    with open(curFile,'w+') as writeFile:
        writeFile.write("Member No Date Joined Active\n")
        data= "{:^13} {:<11} {:<6}"
        date = str(rnd(2000,2020))+ '-' + str(rnd(1,12)) + '-' + str(rnd(1,28))

        writeFile.write(data.format(rnd(10000,99999), date, fee[rnd(0,1)]))
        # writefile.write(data.format(rnd(10000, 99999), date, fee[rnd(0, 1)]))
#
genFile(memReg,exReg)