"""Arithmetic functions module"""

# def add(a,b):
#     return a + b
# def mult(a,b):
#     return a * b
# def div(a,b):
#     return a / b

def add(a,b):
    if type(a) not in (int, float):
        raise TypeError("First argument must be a number")
    if type(b) not in (int, float):
        raise TypeError("Second argument must be a number")
    return a + b

def mult(a,b):
    return a * b

def div(a,b):
    assert type(a) and type(b) in (int, float), " 'b' is not a number"
    if b == 0:
        raise Exception("No division by zero")
    return a / b

if __name__ == '__main__':
    result = div('4',4)
    print(result)

