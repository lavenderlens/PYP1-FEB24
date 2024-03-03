# a dict is a mutable, unordered container of key value pairs
# keys MUST be unique and, ideally, immutable!
# values may be duplicated
# dicts are commonly used to represent complex data

# creation
book = {}
book = dict()

# adding & updating
book['title'] = 'The First Casualty' # <!-- adding a new KV pair
book['title'] = 'Past Mortem' # <!-- overwriting the value with assoc. with the title key
book['author'] = 'Ben Elton'
book['pub_year'] = 1995

# getting a value
title = book['title']

# dict objects have various methods
pub_year = book.pop('pub_year') # <!-- remove the KV pair and return the value
# there are more...

# iterating
for key in book:
    print(key)

for value in book.values():
    print(value)

for key, value in book.items():
    print(key, value)

for key in book:#tricked up to ref values through keys
    print(book[key])
