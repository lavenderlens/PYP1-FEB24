# the == operator is used to test for equality of content
n1 = 1
print('id n1',id(n1))   #4392953000
n2 = 1
print('id n2',id(n2))   #4392953000
print('n1 == n2', n1 == n2) # True

s1 = "Hello"
s2 = "Hello"
print('s1 == s2', s1 == s2) # True

nums1= [1,2,3]
print('id nums1',id(nums1))     #4379972736
nums2= [1,2,3]                  #4380072320
print('id nums1',id(nums2))

print("nums1 == nums2", nums1 == nums2) # True
print("nums1 IS nums2", nums1 is nums2) # False

'''
to understand this result we need to realise 
that the dunder method (DoubleUnderrscore) __eq__()
is overidden in the spec system code for list
no two objects will ever have the same id()
but the __eq__ method of list says that
if two lists have same els in same order they are considered equal

the IS operator tests for equality of id() which will be two separate objects 
beware that the == operator works well for built-in types
but for custom types we nee either to use IS 
or add a __eq__() method to the class defining our custom objects

the IN operator tests for membership and returns a bool
'''

print('2 in nums1', 2 in nums1)#True


d1 = {'x': 1} # dict
d2 = {'x': 1}
print('d1 == d2', d1 == d2) # True
print('d1 IS d2', d1 is d2) # False

dicts1 = [{'x': 1}] # list
dicts2 = [{'x': 1}]
print('dicts1 == dicts2', dicts1 == dicts2) # True
print('dicts1 IS dicts2', dicts1 is dicts2) # False

print('e in Hello', 'e' in 'HELLO'.lower()) # True
