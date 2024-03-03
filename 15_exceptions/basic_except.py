# exceptions - basic example
# user POV: handling means to regain control and carry open
# dev POV: enforcement fo business logic
# without passing an error object or even specifying one 
# we may basically handle this with try/except blocks
try:
    num1 = float(input("enter a number"))
    num2 = float(input("enter a number"))
    total = num1 +num2
    print(total)
except:
    print("Error: something went wrong")
# minimally, this exeception handling code enables the program to carry on
# don't be put off writing code like this if the subtleties of exception handling seem complex to grasp
# this is far, far better than none.
print("end program")