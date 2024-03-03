# sometimes you may want to raise an exception yourself
# why? New devs generally resent spending time fixing the ones they already get!
# Because sometimes stopping or pausing script execution is preferable to the alternatives
# if you are creating objects your business logic may impose rules
# if these rules are flouted, then invalid objecst get into the system

books= [] # mutable

num_books = 1 # immutable

def add_new_book(title, fname, lname):
    if len(fname.strip()) < 3: # bus logic
        raise Exception("The book's author field must be 3 or more characters")
        # common in functions to control for the "sad path" first
    else:
        book = {"title": title, "first name": fname, "last name": lname}
        books.append(book)
        global num_books
        num_books += 1 

add_new_book("Why Whe Drive", "Matthew", "Crawford")
add_new_book("Scary Smart", "Mo", "Gawdat")

print(books, num_books)