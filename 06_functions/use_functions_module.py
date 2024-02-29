# 1 fully qualified
import functions_module
# best choice to eliminate potential naming conflicts

# 2 OR, named
# from functions_module import add, sub, mul, div
# from functions_module import add, sub, mul, div, print

# 3 OR, wildcard 
# from functions_module import *
# reason for NOT using wildcard
# the next dev doesn't know what functions you've used
# and, more importantly
# doesn't know that they are not local functions - dangerous?

# print(functions_module.add(2,2)) # 1

# print(add(2,2)) # 2 and 3

# print(print(2)) # using system value of print() 2 None (value, no return)
# fully-qualified imports 1
print(functions_module.print(42)) # using 2X versions of print()
print(functions_module.print(84)) # from module and from system

