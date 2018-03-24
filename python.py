# Welcome to Python 3 crash course

#Contents
#variables - declaration,user input
num = 5;
country = "India";
user_input = input("Enter a number:")
print("The num you've entered is:",user_input)


#operators - arithmetic, comparison, relational, logical
# +, - , /, *, **
# ==
# <, >, <=, >=
# and, or, not

print(5+6,5*6,5-6,5/6,2**3);


#data types - number, string, list, tuple, dictionary

#number
#int 
 int_num = 5

#float
 float_num = 5.66
  print("Integer Number:",int_num," Float Number:",float_num);

#complex - a+bi

#string
string = "I am Vinayak"
print(string[0])

#list
list1 = [1,2,"Hi",4]
print(list1)
print(list1[1])
list1[2] = 3
print(list1[0:3])

#tuple
tuple1 = (1,3,5,7,"Str")
tuple1[4] = 9  #immutable, will give error 
print(tuple1)

#dictionary
diction1 = {"name":"Vinayak","age":21} ; print(diction1)
print(diction1.keys())
print(diction1.values())


#decision statements - if,elif,else
if(1 == 1): 
    print("true")

if(1 == 1 and 2 == 2):
    print("Both are true")
num = 10
if(num > 20):
    print("More than 20")
elif(num < 10):
    print("Less than 10")
else:
    print("We don't know if the num is >20 or <10")

#loops - for, while

for x in range(0,10):
    print(x)

num = 40
while(num < 45):
    num = num + 1
    print("Less than 45:",num)


#functions - definition, calling

def printName(name):
    print("Your name is:",name)

printName("Vinayak")

#file handling - open(r, w, a), read(), write()

#write
file = open("textfile.txt","w")
file.write("This is a textfile")

#read
file = open("textfile.txt","r")
print(file.read(20))

#append
file = open("textfile.txt","a")
file.write(". Python is awesome!")


