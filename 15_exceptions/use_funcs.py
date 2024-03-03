from funcs import *

a, b  = 3, 7      # add 10 mult 21
# a, b  = '3', '7'  # add 37            force raise error
# a, b  = '3', 7      # mult 3333333      force raise error
# a, b  = 3, "7"      #      

# try:
#     sum_tot = add(a,b)
# except TypeError as e:
#     print(e)
# except:
#     print("some error occurred)")
# else:
#     print(f"Sum is : {sum_tot}")

# product = mult(a,b)
# print(f"Product is : {product}")

division = div(a,b)
print(f"Division is : {division:.2f}")

print("Program end")
