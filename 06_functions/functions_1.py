'''
functions as in any other languae, wrap one or more LOC in a function name
to be called zero, one or many times at some time in the future
how short can a function be?
1 LOC
why? to make the code more declarative

'''

my_str = "Hello"
print(my_str[0]) # grab first character

def firstChar(word):
    print(word[0])

my_str2 = "Goodbye"

firstChar(my_str)
firstChar(my_str2)

# firstChar is a PURE function
# it is IDEMPOTENT - each successive call will result in same output
# one with no side-effects
# what is a side-effect?
# whaen something else outside of the function changes
# resulting in the function output changing
# for THE SAME given input

# functions are objects too, and may be passed as input or returned as output from other functions

char1 = firstChar

char1(my_str)

# functions fall into 4 broad categories depending on whetehr they have:
# input (params)
# output (return statement)
# both
# neither

def greet1():
    print("Hello")
    print("World")
    print("How are you today")

greet1()
# rules of return:
# must be last statement in block
# must return one thing
# though that thing may be a complex expression
# anything under a return statement in the same block is unreachable code
# multiple returns in a function track multiple paths through the function
def greet2():
    return "Hello World \nHow are you \ntoday"

greet2() # can't immediately see output: why?
# value is now passed to the caller from inside the block
#  we can persist the value now, either by assignment to new var OR input to another function
print(greet2())

def greet3(name):
    return "Hello "+ name + " \nHow are you \ntoday"

# print(greet3()) # without an arg: TypeError: greet3() missing 1 required positional argument: 'name

# default arg fixes the above
# now called named args
def greet3(name = "A.N.Other"):
    return "Hello "+ name + " \nHow are you \ntoday"

print(greet3()) # without an arg: TypeError: greet3() missing 1 required positional argument: 'name'

def greet3_positional(name = "John Doe", age = 33):
    return f"""
Hello 
{name}
Today is your birthday! You are {age} today!
"""

print(greet3_positional())#no args, uses default
print(greet3_positional("Alan", 57))#both args, positional
print(greet3_positional(age=57,name="Alan"))#both args, named

def greet4(name, age, employed):
    if employed == False:
        return None
    return f"""
Hello 
{name}
Age {age} 
Employed {employed}
"""
employees = [greet4("fred", 64, False), greet4("John", 44, True)]
print(employees) # [None, '\nHello \nJohn\nAge 44 \nEmployed True\n']
