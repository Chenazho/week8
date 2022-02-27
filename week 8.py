#Jose Lazalde
#Week 8: Working with Files
#Assignment 8.1
#Feb 27, 2022

#The program this week will use the OS library in order to validate that a directory exists before creating a file in
# that directory. Your program will prompt the user for the directory they would like to save the file in as well as
# the name of the file. The program should then prompt the user for their name, address, and phone number.
# Your program will write this data to a comma separated line in a file and store the file in the directory specified
# by the user. Once the data has been written your program should read the file you just wrote to the file system and
# display the file contents to the user for validation purposes.


import os
print(os.getcwd())

def main():
    directory = input("Enter the directory that you want to save the file : ")
    filename = input("Enter the filename : ")
    name = input("Enter your name : ")
    address = input("Enter your address : ")
    phone_number = input("Enter your phone number : ")
#checking if the directory exists
    if os.path.isdir(directory):
#createing and opening the file to write
        writeFile = open(os.path.join(directory,filename),'w')
#writing the data by comma seperated
        writeFile.write(name+','+address+','+phone_number+'\n')
#close the file after writing is done
        writeFile.close()
        print("File contents:")
#reading the file for proof of storing
        readFile = open(os.path.join(directory,filename),'r')
        for line in readFile:
            print(line)
        readFile.close()
    else:
        print("Sorry that directory is not exists, but one will be created")
        os.mkdir(directory)
        writeFile = open(os.path.join(directory, filename), 'w')
# writing the data by comma seperated
        writeFile.write(name + ',' + address + ',' + phone_number + '\n')
# close the file after writing is done
        writeFile.close()
        print("File contents:")
# reading the file for proof of storing
        readFile = open(os.path.join(directory, filename), 'r')
        for line in readFile:
            print(line)
        readFile.close()
main()