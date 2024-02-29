import json
# data in Python:
books = [
    {'title': 'The Gruffalo', 'author': 'Julia Donaldson'},
    {'title': 'The Twits', 'author': 'Roald Dahl'},
    {'title': 'The Bippolo Seed', 'author': 'Dr. Seuss'}
]
# Python >>> JSON
# dumps() is used to convert a list/dict to a JSON string
   #  |  +-------------------+---------------+
   #  |  | Python            | JSON          |
   #  |  +===================+===============+
   #  |  | dict              | object        |
   #  |  +-------------------+---------------+
   #  |  | list, tuple       | array         |
   #  |  +-------------------+---------------+
   #  |  | str               | string        |
   #  |  +-------------------+---------------+
   #  |  | int, float        | number        |
   #  |  +-------------------+---------------+
   #  |  | True              | true          |
   #  |  +-------------------+---------------+
   #  |  | False             | false         |
   #  |  +-------------------+---------------+
   #  |  | None              | null          |
   #  |  +-------------------+---------------+
   #  |  

json_books = json.dumps(books)
print(json_books)
print(type(json_books))
print(json_books[0])

# opposite method, loads(), is used to convert a JSON string into a Python dict or list
books_from_json = json.loads(json_books)
print(books_from_json)
print(type(books_from_json)) # list (OF dicts)
print(books_from_json[0]) # list (OF dicts)

# the dump and load functions are the same but read from and write to JSON

# manipulating JSON

# a context manager simplifies this
# especially when performing ETL (Extract, Transform, and Load):

# 1. Extract from JSON and Transform
with open("./widget.json") as widget_file:

    # read contents of JSON widget into a Python dict
    a_dict = json.load(widget_file)
    print("original widget file", a_dict)

    # make a change/update to the data
    a_dict["widget"]["image"]["src"] = "Images/Moon.png"
    a_dict["widget"]["image"]["name"] = "moon1"
    a_dict["widget"]["text"]["onMouseUp"] = "moon1.opacity = (moon1.opacity / 100) * 90;"

# 2. Load - write modified JSON back
with open("./modified_widget_file.json", mode="w") as modified_widget_file:
    json.dump(a_dict, modified_widget_file)

# 3. ETL insert new nested prop to JSON and write to new file
with open("./widget.json") as widget_file_plus:
    a_dict_plus = json.load(widget_file_plus)
    # a_dict_plus["widget"]["reply"]["confirmation"] = True # KeyError: 'reply' when key is top-level
    a_dict_plus["widget"]["text"]["confirmation"] = True # this syntax works when new key is nested
with open("./modified_widget_file_plus.json", mode="w") as modified_widget_file_plus:
    json.dump(a_dict_plus, modified_widget_file_plus) 

# 4. ETL insert new top level prop to JSON and write to new file
import copy #TODO using deep copy add a new top level branch to json

with open("./widget.json") as widget_file_plus_plus:
    a_dict_plus_plus = copy.deepcopy(json.load(widget_file_plus_plus))
    print(a_dict_plus_plus)

    # a_dict_plus_plus["widget"]["css"]["fontFamily"] = "Helvetica" # still KeyError: 'css'
    a_dict_plus_plus["widget"]["css"] = {'fontFamily': 'Helvetica'} # assign a whole dict to new key
    # https://www.geeksforgeeks.org/python-add-new-keys-to-a-dictionary/

with open("./modified_widget_file_plus_plus.json", mode="w") as modified_widget_file_plus_plus:
    json.dump(a_dict_plus_plus, modified_widget_file_plus_plus) 

# refactor 3 now with correct data shape assigned to new prop and no need for deepcopy()
# this is the one you want, I think, to solve the spec from Thursday's class session
with open("./widget.json") as widget_file_latest:
    a_dict_latest = json.load(widget_file_latest) # no deepcopy necessary now
    a_dict_latest["widget"]["reply"]= {'confirmation': True} # no KeyError
with open("./mod_widget_file_latest.json", mode="w") as mod_widget_file_latest:
    json.dump(a_dict_latest, mod_widget_file_latest) 

