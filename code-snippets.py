# Let's write some code!

"""
This is a multi-line comment.

After running the Python command, the prompt changed to >>>. 
For us this means that for now we may only use commands in the Python language.
"""

# This is a single-line comment.

# The print() function prints the specified message to the screen, or other standard output device.
print("Hello, World!")

# The input() function allows user input.
name = input("What is your name? ")

"""
Math Operators
    Python supports the following operators:
        +	Addition
        -	Subtraction
        *	Multiplication
        /	Division
        %	Modulus
        **	Exponentiation
        //	Floor division

"""
x = 20
y = 4

# Addition
print(x + y)
 
# Subtraction
print(x - y)

# Multiplication
print(x * y)

# Division
print(x / y)

# Modulus
print(x % y)

# Exponentiation
print(x ** y)

# Floor division
print(x // y)


""" 
Python Assignment Operators
    Assignment operators are used to assign values to variables:
        =	    x=5	    x=5
        +=	    x += 3	    x=x + 3
        -=	    x -= 3	    x=x - 3
        *=	    x *= 3	    x=x * 3
        /=	    x /= 3	    x=x / 3
        %=	    x %= 3	    x=x % 3
        //=	    x //= 3	    x=x // 3
        **=	    x **= 3	    x=x ** 3
        &=	    x &= 3	    x=x & 3
        |=	    x |= 3	    x=x | 3
        ^=	    x ^= 3	    x=x ^ 3
        >>=	    x >>= 3	    x=x >> 3
        <<=	    x <<= 3	    x=x << 3
"""


"""
Python Comparison Operators
    Comparison operators are used to compare two values:
        ==	    Equal	                    x == y
        !=	    Not equal	                x != y
        >	    Greater than	            x > y
        <	    Less than	                x < y
        >=	    Greater than or equal to	x >= y
        <=	    Less than or equal to	    x <= y
"""
x=5
y=3
# Equal
print(x == y)

# Not equal
print(x != y)

# Greater than  
print(x > y)

# Less than
print(x < y)

# Greater than or equal to
print(x >= y)

"""
Python Logical Operators
    Logical operators are used to combine conditional statements:
        and 	Returns True if both statements are true	            x < 5 and  x < 10
        or	    Returns True if one of the statements is true	    x < 5 or x < 4
        not	    Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
"""
x = 5
# and
print(x > 3 and x < 10)

# or
print(x > 3 or x < 4)

# not
print(not (x > 3 and x < 10))


"""
Python Identity Operators
    Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, 
    with the same memory location:
        is 	    Returns true if both variables are the same object	    x is y
        is not	Returns true if both variables are not the same object	x is not y
"""
# is
print(x is y)

# is not
print(x is not y)

"""
Python data types
    Built-in Data Types
        Text Type:	    str
        Numeric Types:	int, float, complex
        Sequence Types:	list, tuple, range
        Mapping Type:	dict
        Set Types:	    set, frozenset
        Boolean Type:	bool
        Binary Types:	bytes, bytearray, memoryview

"""

# Getting the data type
x=5
print(type(x))

y = "Hello World"
print(type(y))

z=20.5
print(type(z))

d = {"name": "John", "age": 36}
print(type(d))

"""
Strings
    Strings in python are surrounded by either single quotation marks, or double quotation marks.
    'hello' is the same as "hello".
    You can display a string literal with the print() function:

"""
print("Hello")
print('Hello')

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# Looping Through a String
for x in "banana":
    print(x)

# String Length 
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)


"""
Python Slicing Strings
    You can return a range of characters by using the slice syntax.
    Specify the start index and the end index, separated by a colon, to return a part of the string.
"""
# Get the characters from position 2 to position 5 (not included)
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
b = "Hello, World!"
print(b[:5])


"""
python numbers
    There are three numeric types in Python:
        int
        float
        complex
"""
# Int
x=1    # int
y=35656222554887711    # int
z=-3255522    # int
print(type(x))
print(type(y))
print(type(z))

# Float
x=1.10    # float
y=1.0    # float
z=-35.59    # float

# Complex
x=3+5j
y=5j
z=-5j

"""
Lists
    Lists are used to store multiple items in a single variable.
    Lists are created using square brackets:
"""

# Create a List
thislist=["apple", "banana", "cherry"]
print(thislist)

# Access Items
print(thislist[1])

# Change Item Value
thislist[1] = "blackcurrant"
print(thislist)

# Loop Through a List
for x in thislist:
    print(x)

# Check if Item Exists  
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# List Length
print(len(thislist))

# Add Items
thislist.append("orange")
print(thislist)

# Insert Items
thislist.insert(1, "orange")
print(thislist)

# Remove Item
thislist.remove("banana")
print(thislist)

"""dictionary
    Dictionaries are used to store data values in key:value pairs.
    A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
    As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
    Dictionaries are written with curly brackets, and have keys and values:
"""
# Create and print a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

# Accessing Items
x=thisdict["model"]
print(x)

# Change Values
thisdict["year"]=2018

# Loop Through a Dictionary
for x in thisdict:
    print(x)

# Check if Key Exists
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary") 

# Dictionary Length
print(len(thisdict))

# Adding Items
thisdict["color"] = "red"
print(thisdict)

# Removing Items
thisdict.pop("model")
print(thisdict)

# Copy a Dictionary
mydict=thisdict.copy()
print(mydict)

# Nested Dictionaries
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}

"""
Tuples
    A tuple is a collection which is ordered and unchangeable.
    In Python tuples are written with round brackets.
"""
# Create a Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Access Tuple Items
print(thistuple[1])

# Change Tuple Values
x=("apple", "banana", "cherry")
y=list(x)
y[1] = "kiwi"
x=tuple(y)
print(x)

# Loop Through a Tuple
for x in thistuple:
    print(x)

# Check if Item Exists
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")


"""
Sets
    A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
"""
# Create a Set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Access Items
for x in thisset:
    print(x)


# Add Items
thisset.add("orange")
print(thisset)

# Remove Item
thisset.remove("banana")

# Join Two Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)

"""Errors
    Python has two built-in exceptions to handle errors.
    Syntax Errors
    Exceptions
"""
# Syntax Errors
# print("Hello)
# print("Hello")

# Exceptions
print(10 * (1/0))

"""Error Handling
    The try block lets you test a block of code for errors.
    The except block lets you handle the error.
    The finally block lets you execute code, regardless of the result of the try- and except blocks
"""
# NameError
try:
    print(ex)
except NameError:
    print("Variable ex is not defined")
except:
    print("Something else went wrong")


# DivisionError

try:
    print(10 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
except:
    print("Something else went wrong")


# TypeError
try:
    print("10" + 10)
except TypeError:
    print("You can't add a string and a number!")
except:
    print("Something else went wrong")


"""loops
    Python has two primitive loop commands:
        while loops
        for loops
"""
# The while Loop
i=1
while i < 6:
    print(i)
    i += 1

# The break Statement
i=1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue Statement
i=0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# The else Statement
i=1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# The for Loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# range()
for x in range(10):
    print(x)

# range() with start parameter
for x in range(2, 10):
    print(x)

# range() with start, end and step parameters   
for x in range(2, 30, 3):
    print(x)





"""
    Functions
        A function is a block of code which only runs when it is called.
        You can pass data, known as parameters, into a function.
        A function can return data as a result.
"""


# Creating a Function
def my_function():
    print("Hello from a function")


# Calling a Function
my_function()


# Arguments
def my_function(fname):
    print(fname + " Anne")


my_function("Emil")
my_function("Tobias")


# Number of Arguments
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("John", "Doe")


# Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# Keyword Arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# if the number of keyword arguments is unknown, add a double ** before the parameter name
def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname = "Tobias", lname = "Refsnes")


# Default Parameter Value
def my_function(country = "Uganda"):
    print("I am from " + country)


my_function("Sweden")
my_function()


# Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# Return Values
def my_function(x):
    return 5 * x


print(my_function(3))


# The pass Statement
def myfunction():
    pass


# Recursion
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


tri_recursion(6)


def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')


hi()
hi("Ola")
hi("Ben")




















