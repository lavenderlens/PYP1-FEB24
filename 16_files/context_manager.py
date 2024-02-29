# ensure command prompt is in this dir before running

# context managers open files for reading or writing
# we don't have to close them ourselves
# no need to call read methods
# file is the context
# enter and exit (dunder) functions called under the hood
# instead of having try except to handle errors
# the exit method will handle all the exception handling code-
# no need to write our exception handling !
# may optionally write our own context managers

with open('data.txt') as file:
    for line in file:
        print(f">>> {line}")

with open('data.txt', mode="w") as file: 
    file.write("written with a context manager")

with open('tnsnames.txt') as file:
    content = file.read() # file closed - cursor reset
    print(content) 
    print("cursor automatically reset by context manager\n\n")

# good to go again
with open('tnsnames.txt') as file:
    content = file.read()
    # print(content)

