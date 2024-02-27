# the standard built-in data types

# bool
# values: True or False (or some expression that evaluates to such)
# immutable
my_bool = True 

# int
# values: whole numbers
# immutable
my_int = 1

# float
# values: any fractional number
# immutable
my_float = 1.5

# str
# values: any text of zero or more characters
# immutable
# single or double quotes
# indexed from 0
my_str = 'Hello'
first_character = my_str[0]

# list
# values: the elements in a list can be of any type
# mutable
# indexed from 0
my_list = ['shoe', 'horse', 'pencil']
first_element = my_list[0] # reading the first element - 'shoe'
my_list[1] = 'cat' # overwriting the value at index 1; 'horse' is replaced by 'cat'

# tuple
# values: the elements in a tuple can be of any type
# immutable
# indexed from 0
my_tuple = (42, 'The Meaning of Life')
first_element = my_tuple[0] # reading the first element - 42

# dict
# keys: the keys in a dict may be of any type but are commonly strings; MUST BE UNIQUE
# values: the values in a dict may be of any type and can be duplicated
# mutable
my_dict = {'name': 'Fred', 'age': 33}
name = my_dict['name'] # reading the value associated with the key 'name'
name = my_dict['name'] # reading the value associated with the key 'name'
my_dict['age'] = 34  # re-assign value of age
print(my_dict['age'])  #34

# none
my_none = None