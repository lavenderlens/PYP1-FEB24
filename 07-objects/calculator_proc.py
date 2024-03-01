total = 0

def add(num):
    global total
    total += num
def subtract(num):
    global total
    total -= num
def multiply(num):
    global total
    total *= num
def divide(num):
    global total
    total /= num

def equals():
    global total
    return_value = total
    total = 0
    return return_value


#---
# refactor into a class
# runtime code
add(2)
subtract(4)
multiply(8)
divide(16)
print(equals())
# print(total) # UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
# -1.0

