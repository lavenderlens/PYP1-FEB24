'''
scope defines the visibility and lifespan of a variable
local scope:
-   declared within a function
-   visible only within the function or its blocks
-   lives and dies with the function execution
global scope:
-   declared outside of any functions
-   visible to all functions in the script
-   lives whilst the whole script is executing

'''

next_num = 1

def get_next_num():
    next_num = 1 # NEW, local, var
    next_num += 1
    return next_num

print(get_next_num())
print(get_next_num())# doesn't increment
print("global num", next_num)
# because each time the function executes, it redeclares its local var

def get_next_num_global():
    global next_num # binds the value here to the value in the parent (global) scope
    return_value = next_num
    next_num += 1
    return return_value

print(get_next_num_global())
print(get_next_num_global())
print(get_next_num_global())
print("global num", next_num)

# now, our function REMEMBERS state of next_num through successive invocations
# design problem: what if we wanted to RESET next_num for other function calls?

def get_next_num_encapsulated():
    next_num = 1 # lexically-scoped variable
    def get_next_num():
        nonlocal next_num # binds the value here to the value in the parent (function) scope
        return_value = next_num
        next_num += 1
        return return_value
    return get_next_num # closure (a function and its lexically-scoped variable(s))

my_next_num_closure = get_next_num_encapsulated()
print("using a closure and the nonlocal keyword to bind to function scope")
print(my_next_num_closure())
print(my_next_num_closure())
print(my_next_num_closure())
# in the example with the global keyword binding to global scope
# we could not RESET the function without re-assigning the global var
# here, we can simply create a new closure

my_next_num_closure_2 = get_next_num_encapsulated()
print("making a new closure")
print(my_next_num_closure_2())
print(my_next_num_closure_2())
print(my_next_num_closure_2())

global_name = "Alan"
def test_nonlocal():
    # nonlocal global_name
    global global_name
    global_name = "Kevin"
    return_value = global_name
    return return_value

# print(test_nonlocal()) # SyntaxError: no binding for nonlocal 'global_name' found
print(test_nonlocal()) # 
print(global_name)
# conclusion: the nonlocal keyword may NOT be substituted for global

def global_wrapper():
    global_name2 = "Kevin"
    def test_nonlocal():
        # nonlocal global_name
        global global_name2
        global_name2 = "John"
        return_value = global_name
        return return_value
    return test_nonlocal

global_wrapper_closure = global_wrapper()
print(global_wrapper_closure()) #Kevin
# conclusion: the global keyword MAY be substituted for nonlocal
