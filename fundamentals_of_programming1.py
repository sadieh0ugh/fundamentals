import math

""" PSEUDOCODE: a planning language that can be interpreted into different languages and understood by regular users
                In Exam: assigning a variable is shown as an arrow not '=' """

# COMMENTS: used to explain sections of code that are hard to understand
#           makes code easier to debug

# DATA TYPES:
string = str('apple123@#')
whole_number = int(4)
decimal = float(5.1)  # also called a real
character = char("H") #single character, commonly an ASCII value
boolean = bool(True)

# SETTING DATA TYPES:
# Explicit Data Casting = manually assigning a variable value as a data type e.g.
# Implicit Data Casting = allowing the computer system to

# ARITHMETIC
# + , - , /, *, **  add, minus, divide, times, power
add = 4 + 5 
minus = 4 - 5 
divide = 8 / 2 
times = 4 * 5
exponential = 4 ** 3 # same as 4^3
sqaure = math.sqrt(9)

# ROUNDING:
ans = 9 / 4
print(round(ans,1))  # use round function that has two parameters (variable, decimal place)

#
# TRUNCATING = cutting off a number or string e.g
trun = 9/4
print(math.trunc(trun))

# DIV // = outputs the whole number from division
# 5 DIV 2 = 2

# MOD % = outputs the remainder from the division
# 5 MOD 2 = 1


# STRING HANDLING OPERATIONS

string = 'hello1234'
print(len(string))

char = 'a'
print(ord(char))  # prints number value from ASCII table

num = int(97)
print(chr(num))  # prints ASCII value for variable value


# CONCATENATION - joining two strings together

greeting = 'hello'
name = 'sadie'
concatenated = greeting + name  # '+' does not add a space in between the two words
print(concatenated)

# DIFFERENCE BETWEEN A VARIABLE AND A CONSTANT:
# - constant can't be change but variable an be
# - example of constant, defining pi as 3.14 when calculating circle geometry
# - stored in different memory locations
# - constants save memory because the system knows the value cannot change
#
""" SELECTION: used using relational operators e.g =, ==, <> (not equal to), =! """
#
correct = 4 != 2*3
print(correct)

# IF STATEMENTS: show next line will run after if using :, then, indentation

def percentage(score):
    score = score * 10
    print("You scored",score,"%")

score = int(input("Enter your score out of 10: "))

if score <= 3:
    percentage(score)
    print("Fail, try again")
elif score == 5:
    percentage(score)
    print("Average")
else:
    percentage(score)
    print("Good score")

# ELSE / CATCH ALL STATEMENTS: catches any incorrect inputs

# NESTING: statements inside other statements, using indentations
"""
log = input("username: ")
score = 7
if log == 'sadie':
    if score < 10:
        score = score -1
    else:
elif log == 'tom':
    if score > 10:
        score = score + 1
    else:
        break

else:
    print('invalid')
"""

# ALTERNATIVE SELECTION: Case Statements (in theory exam can write if statements
# Performs different statements

# LOGIC GATES; AND, OR, NOT, XOR

# ITERATION
# WHILE
# REPEAT UNTIL aka DO WHILE: the check of the condition happens at the end of the loop,
#  used if you need to run the code once

number = 0
while number <= 10:
    print(number)
    number = number + 1

# FOR

Nstr = ""
for i in 'hello':
    i= (ord(i)+1)
    Nstr= Nstr + chr(i) # makes shifted letters all into one string
print(Nstr)

Nstr = ""
instring = input(str("Input word to shift: "))
for i in instring:
    i = (ord(i)+1)
    Nstr = Nstr + chr(i)
print(Nstr)

# ELEMENTARY DATA TYPES = single value
# COMPOSITE OR STRUCTURED DATA TYPES = list of multiple values

# ONE DIMENSIONAL ARRAY = list of values with the same data type (exception is python)
# items in an array are referenced in the index[] which starts at 0

onedarray = ['sadie','alice','hough']
print(onedarray[0])

# MULTI-DIMENSIONAL ARRAY = list of arrays
# items referenced with two indexes [][]
# starts with the largest array then descends

twodarray = [['sadie',16,'purple',2001],['ruben',15,2002],['kes',17]]
print (twodarray[0][2]) # returns purple

# ARRAY COMMANDS .append .insert .pop

newname = 'dominic'
onedarray.append(newname)
print(onedarray)

# creates array of 10 0s using while loop
array = []
arraycount = 0
array.append('0')
while arraycount <= 9:
    arraycount = arraycount + 1
    print(array)

# creates 10 lists of 0s using two for loops
array = []
for x in range(1,11):
    line=[]
    for y in range(1,11):
        line.append(0)
    array.append(line)
print(array)


# prints 10 x 10 grid of zeros
array = [['0' for i in range(10)]for i in range(10)]
for i in array:
    line = ""
    for x in i:
        line = line + str(x) + " "
    print(line)


# creates array of 10 alternating 0s and 1s using MODULUS
# ; allows you to append two items
# array = []
size = 10
for i in range(size):
    if i % 2 == 0:
        line1 = []
        for i in range(size):
            num1 = i % 2
            line1.append(num1)
        array.append(line1)
    elif i % 2 == 1:
        line2 = []
        for i in range(1,(size+1)):
            num2 = i % 2
            line2.append(num2)
        array.append(line2)

for i in array:
    line = ""
    for x in i:
        line = line + str(x) + " "
    print(line)

# SUB-ROUTINES = overall term for procedure and function
# piece of reusable code that can be called under a
# FUNCTION returns a value, both can output so always say RETURN
# example of a function is len() because it returns a value

# language defined = what is already built into the language e.g python

# PARAMETERS

# LOCAL AND GLOBAL - scope

# MODULAR PROGRAMMING = breaking down a code into subroutines

''' FILE HANDLING
 record - row of a database
 field - individual piece of data 
  
 text file data base 
 'bob',12,'LG3'
 'sarah',13,'LG2'
  CSF = Comma Separated File
  
  FILE HANDLING COMMANDS:
  file = open('filename.txt', mode) modes = a, r, w 
  
  print(file.readlines()) reads all lines 
  
  lines = ["array", "of", "lines"]
  file.writelines(lines)
  
  after writing / appending to a file must use file.close()
  
EXCEPTION HANDLING: two commands are: try, except 
- set exception as e 
 
'''

# EXCEPTION HANDLING EXAMPLE

choice = input("Press 1 to login\n\
Press 2 to signup\n\
Press 3 to close\n")
while choice <'1' or choice > '3':
    try:
        number = int(input)
    except:
        print("must be an integer between 1 and 3")
    break
