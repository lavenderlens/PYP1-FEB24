'''The rectangle module.'''

def area(length, width):
    return length * width
def perimeter(length, width):
    return 2 * (length + width)
# utility functions
def cms_to_inches(cms):
    return cms * 0.39
def inches_to_cms(inches):
    return inches * 2.54

# we may control what is imported on the wildcard import
# we may still request the others, but have to do so explicitly
__all__ = ['area','perimeter']


