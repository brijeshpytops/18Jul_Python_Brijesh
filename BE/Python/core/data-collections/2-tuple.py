"""
Tuple : Ordered, immutable, duplicate values are allowed, indeing, slicing

A tuple is an ordered collection of items. It is an immutable data type in Python, meaning its elements cannot be changed after they are created.

Syntax:

tuple_name = (value1, value2, value3,...)
tuple_name = tuple()
comma_tuple = 12,
"""

# nums = (1, 2, 3, 4)
# nums = 1,
# print(type(nums))

# indexing (+/-)

# nums = (1, 2, 3, 4, 5)

# print(nums[2]) # 3

# slicing (:)

# print(nums[1:3]) # (2, 3)

# print(nums[:3]) # (1, 2, 3)

# print(nums[2:]) # (3, 4, 5)

# nums = (1, 2, 3, 4, 5, 1, 1)
# print(nums)


# nums = tuple()
# print(dir(nums))

# 'count', 'index'

# nums = (1, 2, 3, 4, 5)

# nums[0] = 11 # TypeError: 'tuple' object does not support item assignment

# print(nums) 