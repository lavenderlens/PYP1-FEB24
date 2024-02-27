'''
conditional statements are very smilar in Python to other langauges,
they execute a block of code depending on whether a condition evaluates True or False
if True:
code bolck, defined by indent, immediately following is executed
if False:
skipped

an else block has NO condition and means, really ANYTHING else

you can test multiple conditions using if elif else

following execution of a branch the interpreter steps out of the statement structure, like a break

so when using ranges of values, if..elif blocks should be arranged with care to avoid unreachable code

Since recently in Python 3.10 there is another decision control statement
Called Structural Pattern Matching or match case
This mimicks the behaviour of switch in Java and JS, which traditionally has had no equivalent in Python
The match statemnt tests a single variable or expression for equality

'''

# one branch
if False:
    print("IF block executed")

# two branch
if False:
    print("SECOND IF block executed")
else:
    print("ELSE block executed")

# three or more branches
if False:
    print("SECOND IF block executed")
elif True:
    print("ELIF block executed")
else:
    print("ELSE block executed")

print("carrying on as usual...")

# an if else may be written on one line
# it mimicks the ternary operator in other langs
# ternary is a form of exclusive or - one or other part may be true
#BUT both may not be true or false

temp = 'cold'
clothing = 'jumper' if temp == 'cold' else 'T-shirt'

