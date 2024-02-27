# console: the machine in front of you; composed of stdin and stdout
# stdin: standard in is typically the keyboard
# stdout: standard out is typically the screen

# function: a name associated with a group of statements
# to call a function is to execute the statements assoc. with the function name

# the built-in print function is used to write to stdout, e.g.
print('Hello')

# the built-in input function is used to read from stdin, e.g.
name = input('Enter your name: ')

# the print function can accept many arguments, not just one
# each argument will be delimited by a space by default
print('Your name is', name)

# in this example print, input and name are all names of things
# print and input are names of functions
# name is the name of some data (whatever the user types at the prompt)
# names are not like boxes containing stuff; instead they are like signposts (names actually contain addresses)

# correct datatype
age = int(input('Enter your age: '))
print('Your age is: ' + str(age))

# or as strings will encode 9 3/4 etc
# age = input('Enter your age: ')
# print('Your age is: ' + age)