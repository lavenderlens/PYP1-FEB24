s1 = "Hello"
s2 = "Hello"
print(id(s1))
print(id(s2))

s3 = str("Goodbye")
s4 = str("Goodbye")
print(id(s3))
print(id(s4))

# number formatting in strings

import math
print(math.pi)
print(f'PI to two dec. places = {math.pi:.2f}')
price = 19.990
print(f'price in pounds and pence = {price:.2f}')
price_int = 20
print(f'price in pounds and pence = {price_int:.2f}')

price_string = "price in pounds and pence = 19.99"
print(price_string[0:5])
print(price_string[-1:6]) # you cant do this, mix neg and pos this way round
# print(price_string.index("1"))
print(price_string[-1:price_string.index("1"):-1]) # with a step
print(price_string[price_string.index("pounds"):]) # 