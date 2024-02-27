'''
The wlarus operator := makes an assignment AND returns that value at the same time,
making for succinct code that nonetheless requires knowledge to read
but can cut down on boilerplate code which would otherwise need several separate lines
'''

# in interactive session, if I assign False/True, there will be no output
walrus = True
# however if we wrap a normal equals assignment in brackets
# Python does not recognise the syntax
# (walrus = True) # SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
# if we use the walrus it assigns AND returns
# but MUST be wrapped in round brackets grouping operator
value_of_walrus = (walrus := True)
print(value_of_walrus) # True

# use case could be simplifying loop logic
words = []
while (word := input("Enter a word or type quit to exit:")).lower() != "quit":
    words.append(word)

# old school equivalent:
words2 = []

while True:
    word = input("Enter a word or type quit to exit:")
    if word.lower() != "quit":
        words2.append(word)
    else:
        break