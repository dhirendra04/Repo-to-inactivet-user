# this file contain use of format function

name_var = 'Dheeren'

print("1. my name is Dheeren")

print("2. my name is {}".format(name_var))

no1 = 10
no2 = 20

print("my number 1 = {} and my number 2 = {}".format(no1, no2))

a = 30
b = 20
c = 10

#print("  val of c = {} and value of a = {} and value of b = {}".format(a,b,c))
#print("* val of c = {2} and value of a = {0} and value of b = {1}".format(a,b,c))
#print("value of b{0} and value of a{1} and value of c{2}".format(a,b,c))
#print("value of a{2} and value of b{1} and value of c{0}".format(c,b,a))

line1 = "value of a{2} and value of b{1} and value of c{0}".format(c,b,a)
print(line1)
