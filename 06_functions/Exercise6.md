### Exercise 6 - functions again

Create a file named ex6_script.py.

Code and test simple functions as follows:

get_greeting that returns a greeting, e.g. G'day

get_greeting_to that accepts a name and returns G'day [`name`]

get_product that accepts two numbers and returns the product of those numbers

get_first that accepts a list and returns the first element

get_name that accepts a dict and returns the value assoc. with the name key

get_circumference that accepts a radius and returns the circumference

If you're feeling adventurous...

Create a file named ex6_module.py.
Then separate out just your functions, and put them in this new file.
Then import them into ex6_script.py where they will be called by your existing runtime code.

HINT: There are three ways of importing functions

`import ex6_module`

#### but the wildcard \* means funcs do not need to be called by module name

`from ex6_module import *` # best NOT to do this but to import on a function-by-function basis

`from ex6_module import get_greeting, get_greeting_to, get_product, get_first, get_name, get_circumference`
