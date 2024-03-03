# circumstances where we make wish to raise an exception ourselves
import math
import KevinError
# module or definition time
def circ(radius):
    if type(radius) == int or type(radius) == float:
        return 2 * math.pi * radius
    else:
        # 1. raise TypeError("Enter numbers only") # custom error here?
        raise KevinError.KevinError("Enter numbers only") #
        # catches error before runtime, stops execution

print(math.pi)
# runtime
# try: # 1.
#     print(circ("1"))
# except KevinError.KevinError:
#     print("Ooops something went wrong")
# catches error AT runtime, allows for recovery
    
print(circ("1")) # 2. error now caught in the function, output:
# KevinError.KevinError: Enter numbers only

print("Carrying on...") # can't carry on when exception caught in method
