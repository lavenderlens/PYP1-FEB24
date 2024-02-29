# import shapes # 1. this is attempting to import a whole package AS A ++MODULE++
# AttributeError: module 'shapes' has no attribute 'circle'

# from shapes.circle import *  # 2. works but do not use
# that's import * from the ++MODULE++ not the whole package

# import shapes.circle  # 3. works, can use

from shapes import circle # 4. BEST, 
# then usage is qualified by MODULE but not by package

from shapes.rectangle import * # wildcard 
# will not import cms_to_inches or inches_to_cms
from shapes.rectangle import cms_to_inches # >>>
# explicitly ask for utility methods
# otherwise encapsulated by __all__ dunder method in module

rad = 10
# circle1 = circumference(rad)  # 2.
# circle1 = shapes.circle.circumference(rad)  #3.
circle1 = circle.circumference(rad)  #4. preferred syntax - module name up front but not package name
print(circle1) # 62.83185307179586
rect1 = area(2,5)
rect2 = perimeter(2,5)
print(rect1, rect2)
print(cms_to_inches(6))
# inches_to_cms(2.34) # >>>
# not available unless specifically asked for

# https://docs.python.org/3/tutorial/modules.html