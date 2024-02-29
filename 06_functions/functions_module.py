'''
a module is any Python script that containes only 
variables, 
functions, and 
classes
These may be called from a runtime that would then be uncoupled from the declarations
'''

def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    if num2 == 0:
        return None
    return num1 * num2
def print(num):
    # print(num) # RecursionError: maximum recursion depth exceeded
#     # above error thrown here not in runtime 
#     # this function thinks 
#     # this is tail call!
#     # because its scope lookup is the immediate function scope
#     # parent scope in this script takes precedence over system version
#     # so make it return instead of print  
    return f'you entered: {num}'

if __name__ == '__main__':
    print("You only see me if you run the module")