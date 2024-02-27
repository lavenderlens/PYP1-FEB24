name = input("enter your name >>")
print("Hello " + name + ", how are you?")
print("Hello {}, how are you?".format(name))
print(f"Hello {name}, how are you?")

age = input("Enter your age >>")
print(type(age))

print("Hello " + name + ", you are " + age + " years old.") # age is actually a str type
# print("Hello " + name + ", you are " + (age + 1) + " years old next year.") # ERR: 1 is the int type
# TypeError: can only concatenate str (not "int") to str
print("Hello " + name + ", you are " + str(int(age) + 1) + " years old next year.") # age converted into int, 1 added, converted back again
print("Hello {}, you are {} years old.".format(name, age))
print(f"Hello {name}, you are {age} years old.")

age = int(age)
print(type(age))

# print("Hello " + name + ", you are " + age + " years old next year.")#TypeError: can only concatenate str (not "int") to str
print("Hello " + name + ", you are " + str(age + 1) + " years old next year.")#TypeError: can only concatenate str (not "int") to str
print("Hello {}, you are {} years old next year.".format(name, age + 1))
print(f"Hello {name}, you are {age + 1} years old next year.")

# version numbers:
# CONCATENATION: < 3
# PLACEHOLDERS WITH .format(): > 3
# PLACEHOLDERS WITH f-strings: > 3.5
# PLACEHOLDERS WITH f-strings and triple quotes (preserving line breaks): > 3.7

# DICTIONARIES VERSIONING
# As of Python version 3.7, dictionaries are ordered. 
# In Python 3.6 and earlier, dictionaries are unordered.


