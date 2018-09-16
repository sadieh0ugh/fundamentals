
import math
""" PSEUDOCODE: a planning language that can be interpreted into different languages and understood by regular users
                In Exam: assigning a variable is shown as an arrow not '=' """

# COMMENTS: used to explain sections of code that are hard to understand
#           makes code easier to debug

# DATA TYPES:
string = str('apple123@#')
whole_number = int(4)
decimal = float(5.1)  # also called a real
# character = char("H") #single character, commonly an ASCII value
boolean = bool(True)

# SETTING DATA TYPES:
# Explicit Data Casting = manually assigning a variable value as a data type e.g.
# Implicit Data Casting = allowing the computer system to

# ARITHMETIC
# + , - , /, *, **  add, minus, divide, times, power
#
# ROUNDING:
ans = 9 / 4
round(ans,2)  # use round function that has two parameters (variable, decimal place)
print(ans)
#
# TRUNCATING = cutting off a number or string e.g
trun = 9/4
trun = math.trunc(1)
print(trun)  ### need to fix this

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
concatenated = greeting + name # '+' does not add a space in between the two words
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

x = 'string'


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

#FOR

Nstr=""
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
while arraycount <= 9:
    arraycount = arraycount + 1
    array.append('0')
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


# creates array of 10 alternating 0s and 1s
# ; allows you to append two items

for x in range(0,5):
    array.append(0);array.append(1)
print(array)









