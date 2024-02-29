'''
args - multiple positional arguments
denoted in parentheses as *args
the word args is arbitrary
the * is mandatory
kwargs - multiple named (keyword) arguments
denoted in parentheses as **kargs
the word kargs is arbitrary
the ** is mandatory
'''

def greet(name, *hobbies):
    print(f"Hello from {name}")
    print(f"I like")
    print(f"{hobbies}")

greet("Alan", "music", "photography") #tuple: ('music', 'photography')
greet("Billy")
greet("Kevin", "more coding", "coding", "coding in a new language")

# what if we wish to pass named arguments, not positional?

def greet(name, *hobbies, **other_details):
    print(f"Hello from {name}")
    print(f"I like")
    print(f"{hobbies}")
    print(other_details)

greet("Alan", "music", "photography", county="Donegal", country= "Ireland", eu_member = True)
# kwargs packed into dictionary {'county': 'Donegal', 'country': 'Ireland', 'eu_member': True}
greet("Kevin", county="Manchester", country= "England", eu_member = False)
# greet("Billy", county="Manchester", country= "England", eu_member = False, name="a name")#error TypeError: greet() got multiple values for argument 'name'
greet("Billy", county="Manchester", country= "England", eu_member = False)# we could directly modify kwargs object it it were returned and not printed #TODO - classes


