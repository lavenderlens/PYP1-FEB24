num = 1
num_copy = num
num_copy += 1
print(num_copy)
print(num) # 1 - unaffected
# the above copies a reference to an immutable object
# the below copies a reference to an MUTABLE object
lst = [1,2,3]
lst_copy = lst
lst_copy.append(4)
print(lst_copy)
print(lst) # [1, 2, 3, 4] original changed

import copy

lst_shallow_copy = copy.copy(lst)
lst_shallow_copy.append(5)
print(lst_shallow_copy)
print(lst) # [1, 2, 3, 4] looks good but we can still break it at other levels of recursion/nesting

lst_in_list = [[1,2,3], [4,5,6]]
lst_in_list_shallow_copy = copy.copy(lst_in_list)
lst_in_list_shallow_copy.append([7,8,9])
print(lst_in_list_shallow_copy) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lst_in_list) # [[1, 2, 3], [4, 5, 6]]

lst_in_list_shallow_copy[1].append(7)
print(lst_in_list_shallow_copy) # [[1, 2, 3], [4, 5, 6, 7], [7, 8, 9]]
print(lst_in_list) # [[1, 2, 3], [4, 5, 6, 7], [7, 8, 9]]

lst_in_list_deep_copy = copy.deepcopy(lst_in_list_shallow_copy)
print(lst_in_list_deep_copy[2])
lst_in_list_deep_copy[2].append(10) 
del lst_in_list_deep_copy[1][3] 
print(lst_in_list_deep_copy) # [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
print(lst_in_list_shallow_copy) # [[1, 2, 3], [4, 5, 6, 7], [7, 8, 9]]
