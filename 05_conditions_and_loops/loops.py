'''
Loops come in two sorts: the while loop and the for loop.
Every for loop in Python compiles into a while loop.
the while loop is the underlying structure.

while loops nonetheless are commonly used for console IO
for loops are commonly used to iterate over containers
usually when the number of iterations is known in advance
either from the len() prop of the container
or from a hardcoded value passed in to the range() function

diff:

in Python, an optional else clause may be added to the end of a loop
this works for both types for and while
it will only be excuted if the ;loop runs to completion
ie doesn't encounter a break statement

'''

# for is used for stepping through an iterable, usually a container type

names = ['Michael Jackson', 'David Bowie', 'Janet Jackson', 'James Brown',\
         'Gordon Brown', 'David Hume']

names_set = {'Michael Jackson', 'David Bowie', 'Janet Jackson', 'James Brown',\
         'Gordon Brown', 'David Hume'}

names_tuple = ('Michael Jackson', 'David Bowie', 'Janet Jackson', 'James Brown',\
         'Gordon Brown', 'David Hume')

# list and set are mutable, tuple is not

names[len(names) - 1] = 'David Byrne'
print(names)

# names_tuple[len(names_tuple) - 1] = 'David Byrne' # TypeError: 'tuple' object does not support item assignment

print('AS LIST')
for name in names:
    print(name)
print('AS SET')
for name in names_set:
    print(name)
print('AS TUPLE')
for name in names_tuple:
    print(name)

# make list of unique surnames 
# using set() to create an empty set
# using set.add()to add to a set in a loop
# using str.split() on default space character to obtain surname
unique_surnames = set()
print(type(unique_surnames))
# then in a loop split each original list member and add second part to set
print("using split on comma:")
csv_names = ['Michael,Jackson', 'David,Bowie', 'Janet,Jackson', 'James,Brown',\
         'Gordon,Brown', 'David,Hume']
for name in csv_names:
    # unique_surnames.add(name.split(',')[1])#TODO - fixed, 1 positional arg (what to split on)
    unique_surnames.add(name.split(sep=',')[1])# or named arg
print(unique_surnames)

# we could use a while loop to iterate round our names collection/list
# but it's a less elegant way than the for
index = 0
while index < len(names):
    print(names[index].split()[0])
    # must do this:
    index += 1

#  while is equivalent to for and for compiles down into while
    #  but while is more suited to iterative scenarios where the number of iterations is not or can't be worked out in advance

print("enter any song to add to the setlist or 0 to quit")
songs = ""
song = ""
while True:
    song = input("Song title")
    if song == "0":
        break
    songs += song + ", "

print(songs)

# the range function:
for number in range(1,10,2):
    print(number)

# break and continue with optional else
print("using break)")
for name in names:
    if name == "Janet Jackson":
        break
    print(name)
else:
    print("all done!")

print("using continue)")
for name in names:
    if name == "Janet Jackson":
        continue
    print(name)
else:
    print("all done!") # the loop has run to completion
