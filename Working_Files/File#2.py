from random import randint as rnd
memReg = 'C:\\Users\\suneel\\OneDrive\\Desktop\\members.txt'
exReg = 'C:\\Users\\suneel\\OneDrive\\Desktop\\inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))



def cleanFiles(currentMem, exMem):
# TODO: Open the currentMem file as in r+ mode
    with open(currentMem, 'r+') as writeFile:
        with open(exMem, 'a+') as appendFile:
            writeFile.seek(0)

    # TODO: Read each member in the currentMem (1 member per row) file into a list.
            members = writeFile.readlines()
    # Hint: Recall that the first line in the file is the header.
            header = members[0]
            members.pop(0)
    # TODO: iterate through the members and create a new list of the innactive members
    #         inactive = [member for member in members if ('no' in member)]
            for member in members:
                if 'no' in member:
                    inactive = member
            print(inactive)
    # Go to the beginning of the currentMem file
            writeFile.seek(0)
            writeFile.write(header)
            for member in members:
                if(member in inactive):
                    appendFile.write(member)
                else:
                    writeFile.write(member)
            writeFile.truncate()
    # TODO: Iterate through the members list.
    # If a member is inactive, add them to exMem, otherwise write them into currentMem

genFiles(memReg,exReg)
cleanFiles(memReg,exReg)