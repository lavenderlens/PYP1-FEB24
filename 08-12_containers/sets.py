# a set is a mutable, unordered container that DOES NOT permit duplicate elements
# sets are commonly used to strip duplicates from lists

# creation
unique_nums1 = {1, 1, 2, 2, 3, 3, 3}
unique_nums2 = set([1, 1, 2, 2, 3, 3, 3])

# from set back to list
nums_list = list(unique_nums2)

# NB: sets DON'T work with dicts (or other mutable built-in types)

# sets have some cool methods
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1.intersection(set2) # {3, 4}
set4 = set1.difference(set2) # {1, 2}
set5 = set1.symmetric_difference(set2) # {1, 2, 5, 6}