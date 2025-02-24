"""
What is list in python?

LIST : ordered, mutable, duplicates values are allowed, indexing, slicing

A list is an ordered collection of items. It is a mutable data type in Python, meaning its elements can be changed after they are created.

syntax:

list_name = [value1, value2, value3,...]
list_name = list()
"""

# nums = [1,2,3,4]

# print(len(nums))

# print(type(nums))

# mix_list = [10, 20, 34.67, 'python', 534 + 3645j]
# print(mix_list)

# nums = [1,1,2,3,4,5, 5]

# print(nums)

items = ['tomato', 'potato', 'onion', 'guava', 'grapsh']
# print(items)

# indexing (+/-)
# print(items[2])
# print(items[4])
# print(items[-1])
# print(items[-4])

# slicing (+/-)
# print(items[:])
# print(items[2:])
# print(items[:3])
# print(items[::2])
# print(items[::-1])
# print(items[:-3:-1])

# concat

# new_items = items + ['carrot', 'mango']

# print(new_items)

# replica

# new_items = items * 2

# print(new_items)

# print(dir(list()))



nums = [1,2,3,4,5]
new_nums = [6,7,8,9,10]
# num = [1111]

# add

# nums.append(new_nums) # [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]
# nums.extend(new_nums) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nums.insert(2, new_nums) # [1, 2, [6, 7, 8, 9, 10], 3, 4, 5]
# nums.insert(2, num)
# print(nums)

# delete
# nums.pop() # 5 remove
# nums.pop(2)
# nums.clear()
# nums.remove(4)

# del nums[1]
# print(nums)

nums = [1,2,3,4,5, 1, 2, 1]
# print(nums.count(1))

# print(nums.index(3))
# print(nums.index(1, 6))

# copy_nums1 = nums.copy()
# copy_nums2 = nums


# print(copy_nums1)
# print(copy_nums2)
# print(id(nums))
# print(id(copy_nums1))
# print(id(copy_nums2))
# nums.reverse()
# nums.sort(reverse=True)
# print(nums)

nested_list = [1,2,[3,4,[5,6,[7,8,[9,10,[11], 12]]]]]
print(nested_list[-1])
print(nested_list[-1][-1])
print(nested_list[-1][-1][-1])
print(nested_list[-1][-1][-1][-1])
print(nested_list[-1][-1][-1][-1][-2])
print(nested_list[-1][-1][-1][-1][-2][-1])
print(nested_list[-1][-1][-1][-1][2][-1])

