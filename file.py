# This file contain file operation like open , create, read, write, append

# function name "open"

# w = write mode
# r = read mode (defult)
# a = append mode
# w+ = ?
# r+ = ?
# a+ = ?

myfile = open("abc.txt", 'a')
myfile.write("this is line1\n")
myfile.close()

myfile = open("abc.txt", 'r')
var = myfile.readlines()
print(var)
myfile.close()


# myfile = open("abc.txt", 'a+')
#
# myfile.write("this is line1\n")
#
# myfile.seek(0)
# var = myfile.readlines()
#
# print(var)
#
# myfile.close()
