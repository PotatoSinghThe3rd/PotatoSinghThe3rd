# variable = a container for a value. Behaves as the value that it contains.

#First_Name = 'Ethan'
#Last_Name = 'Singh'
#Full_Name = First_Name + " " + Last_Name
#print("hey " + Full_Name)
#print(type(name))

# the integer data type stores whole numbers.
#age = 7
#age += 1
#print("your age is: " + str(age))
#print(type(age))

# float data type can store decimals points unlike integers.

#height = 250.5
#print("your height is: " +str(height)+"cm")
#print(type(height))

# boolean is a variable that can only store true or false. Very useful for if statements.

#human = True
#print(human)
#print("are you a human: "+str(human))
#print(type(human))

# multiple assignment = allows us to assign multiple variables at the same time in one line of code.

#name = "ethan"
#age = 7
#attractive = True

#print(name)
#print(age)
#print(attractive)

#name, age, attractive = 'ethan', 7, True
#print(name, age, attractive)

#spongebob = patrick = sandy = squidward = 30
#print(spongebob)
#print(patrick)
#print(sandy)
#print(squidward)

# string methods:

#name = "ethan"
#print(len(name))
#print(name.find("a"))

# can only capitalize the first letter of string.
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("a"))

# splits string with spaces
#name.split()
#name.title()
#print(name.replace("a", "o"))
#print(name*3)

# type casting = convert the data type of a value to another data type.

#x = 1       #int
#y = 2.0     #float
#z = "3"     #str

#permanent
#x = float(x)
#y = int(y)
#z = int(z)

#temporary
#print(x)
#print(int(y))
#print(int(z))

# user input

#name = input("What is your full name?: ")
#print(name)
#age = int(input("How old are you?: "))
#height = float(input("how tall are you?: "))
#ID = input("What is your ID?: ")

#print("Hello "+(name))
#print("You are "+str(age)+" years old")
#print("You are "+str(height)+("cm tall"))
#print("ID number and verification: "+ str(ID))

# math functions

#always remember to IMPORT math
#import math

#pi = 3.14
#x = 1
#y = 2
#z = 3

# print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))

# tells you how far away it is from 0
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(pi))

#print(max(x,y,z))
#print(min(x,y,z))

# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

#name = "Ethan Singh"

#first_name = name[:6]          # [0:6]
#last_name = name[6:]           # [6:end]
#funky_name = name[::2]         # [0:end:2]
#reversed_name = name[::-1]     # [0:end:-1]

#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)

#website1 = "http://google.com"
#website2 = "http://wikipedia.com"

#slice = slice(7, -4)

#print(website1[slice])
#print(website2[slice])

# if statement = a block of code that will execute if its condition is true

#age = int(input("How old are you?: "))

#if age == 100:
#    print("You are a century old!")
#elif age >= 18:
#    print("You are a Adult!")
#elif age < 0:
#    print("You haven't been born yet!")
#else:
#     print("You are a child!")

# logical operators (and,or,not) = used to check if two or more conditional statements is true

#temp = int(input("what is the temperature outside?: "))

#if not(temp >= 0 and temp <= 30):
#    print("The weather is good today!")
#    print("go outside!")
#elif not(temp < 0 or temp > 30):
#    print("The weather is bad today!")
#    print("stay inside!")

# while loop = a statement that will execute its block of code,
#              as long as its condition remains true

#name = input("Enter your name: ")

#while len(name) == 0:
#    name = input("ENTER YOUR NAME: ")

#name = (name.title())
#print("Hello Mr."+name)

# for loop =    a statement that will execute its block of code
#               a limited amount of times

#               while loop = unlimited
#               for loop = limited

#for i in range(10):
    #print(i + 1)

#for i in range(50,100+1,2):
    #print(i)

#for i in "Ethan Singh":
    #print(i)

#always remember to IMPORT time
#import time

#x = int(input("select how many seconds: "))
#for seconds in range(x,0,-1):
    #print(seconds)
    #time.sleep(1)
#print("Happy Birthday!")

# nested loops =    The "inner loop" will finish all its iterations before
#                   finishing one iteration of the "outer loop"

#rows = int(input("How many rows?: "))
#columns = int(input("How many columns?: "))
#symbol = input("Enter a symbol: ")

#for i in range(rows):
#    for j in range(columns):

#  (end="") prevents the cursor from moving to the next line
#        print(symbol, end="")

#  prints new line
#    print()

# Loop Control Statements = change a loops execution from its normal sequence

# break =       used to terminate loop entirely
# continue =    skips to the next iteration of the loop
# pass =        does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#   (!=) means (does not)
#     if name != "":
#         break

# name = name.title()
# print("Hello Mr. " +name)

#phone_number = input("Enter your phone number (123-456-789): ")

#for i in phone_number:
#    if i == "-":
#        continue
#    n = print(i, end="")

#print(" is your phone number")

#for i in range(1,21):
#    if i == 13:
#         pass
#     else:
#         print(i)

# list = used to store multiple items in a single variable

#food = ["Broccoli", "Daal rice", "Paratha", "Cheese"]

#food[0] = "Scrambled eggs"

# list functions
#food.append("Besan Halwa")
#food.remove("Paratha") or food.remove(food[2])
#food.pop()
#food.insert(0,"Poha")
#food.sort() # will sort alpha and ints
#food.clear()

#for i in food:
    #print(i)

# 2D lists = a list of lists

#drinks = ["Water", "Milkshake", "Coffee"]
#breakfast = ["Scrambled Eggs", "Avocado Toast", "Poha"]
#dessert = ["Cake", "Ice Cream"]

#food = [drinks, breakfast, dessert]

#print(food[1][0])

# tuple =   collection which is ordered and unchangeable
#           used to group together related data

#student = ("Ethan",7,"Male")

#print(student.count("Ethan"))
#print(student.index("Male"))

#for i in student:
    #print(i)

#if "Ethan" in student:
    #print("Ethan is in the tuple!")

# set = collection which is unordered, unindexed. No duplicate values.
#       basically random order and doesn't print duplicates of anything

utensils = {"Fork", "Knife", "Spoon"}
dishes = {"Bowl", "Plate", "Cup"}

# utensils.add("Napkin")
# utensils.remove("Spoon")
# utensils.clear()
utensils.update(dishes)


for i in utensils:
    print(i)










