# a list is a mutable, indexed (ordered) container that permits duplicate elements
# lists are commonly used to store groups of objects of the same type

# creation
nums = list() # <!-- list is the class
nums = [1, 2, 3]

# indexing
first_num = nums[0] # <!-- read
nums[2] = 4 # <!-- overwrite

# slicing: the creation of a new list that is a subset of another
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# the first number is the starting index (incl.)
# the second number is the ending index (excl.)
slice1 = fib[4:8] # [3, 5, 8, 13]

# the third number is the step/increment
slice2 = fib[4:8:2] # [3, 8]

# if no index is specified then the start is assumed to be 0, and the end is assumed to be len
# the result of this is a version of the list with the elements in reverse
slice3 = fib[::-1]

# list objects have various methods
nums.append(8) # <!-- adds to the end of the list
nums.remove(1) # <!-- removing the first instance of the number 1
# there are lots more...

# iterating
for num in nums:
    print(num)

# built-in methods
num_elements = len(nums)
sum_of_elements = sum(nums)
min_element = min(nums)
max_element = max(nums)

# arithmetic
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

nums3 = nums1 + nums2 # [1, 2, 3, 4, 5, 6]
nums4 = nums1 * 2 # [1, 2, 3, 1, 2, 3]
# etc.