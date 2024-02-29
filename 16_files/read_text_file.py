# to run this file ensure that command prompt is in this directory
# for relative file paths:
# Python will look in current working directory first
# but VSC will look in its top-level project directory

file = open("tnsnames.txt")
print(type(file)) # <class '_io.TextIOWrapper'>

print(dir(file))
# 1. read()
# 2. readline()
# 3. readlines()

# 1. read() or read(chars)
# content = file.read() # default no args read reads all, when end reached data no longer available
# print(content)  
# cursor reads from where it last finished
# (this "carries over" to calling read(chars), readline() below)
# some_content = file.read(100) # default no args read reads all
# print(some_content) 
# print(type(some_content)) 

# 2. readline()
# line = file.readline()
# print(line)
# line = file.readline()
# print(line)
# line = file.readline()
# print(line)
# line = file.readline()
# print(line)

# 3. readlines()
# lines = file.readlines()
# print(lines) # returns list of csv strings with newline characters
# for line in lines:
#     print(line.split('\n')[0]) #re-assembled it by ignoring the newline characters

# we can also iterate throught the Files object 
    # yields one line at a time
for line in file:
    print(line)

# ---
file.close()

# 