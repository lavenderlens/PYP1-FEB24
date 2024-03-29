# lst=[] # needs explicitly re-assigned in order to reset
def outer_a():
    lst = [] # ignored by global keyword
    def add_to_lst(item):
        nonlocal lst
        return_value = lst
        lst.append(item)
        return return_value
    return add_to_lst

my_closure = outer_a() # makes closure and is able to be easily reset by repeating it
print(my_closure("Alan"))
print(my_closure("Kevin"))
print(my_closure("John"))
# print(lst)  # out of global scope - therefore encapsulated
# print(lst)  # empty when global lst declared