my_tuple = ("name", 21, ["walking", "photography"], True)
my_tuple_strings = ("name", "21", "[\"walking\", \"photography\"]", "True")
my_tuple_numbers = (1,3,5,7,9)

# print(max(my_tuple))
# print(min(my_tuple))

# err 1 TypeError: '>' not supported between instances of 'int' and 'str'

print(max(my_tuple_strings)) # name
print(min(my_tuple_strings)) # 21
print(max(my_tuple_numbers)) # 9
print(min(my_tuple_numbers)) # 1