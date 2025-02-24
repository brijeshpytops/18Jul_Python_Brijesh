"""
function:

syntax:

def function_name(para1, para2, ...paran): # function defination
    body of function

function_name(val1, val2, ...valn) # function call 


"""

# a = 10
# b = 20
# c = a + b
# print(c)

# d = 30
# e = 40
# f = d + e
# print(f)

# 100 * 4 = 400

# def add(num1, num2):
#     # print(num1 + num2)
#     return num1 + num2

# print(add(10,20))
# print(add(30,40))

# type of parameters/args
# 1] positional
# def add(num1, num2, num3):
#     return num1 + num2 + num3

# print(add(10,20)) # TypeError: add() missing 1 required positional argument: 'num3'


# 2] default/keywords
# def info(name, age=30):
#     print(name)
#     print(age)

# info("brijesh")
# info("brijesh", age=50)
    
# 3] variable length args
# *args
# **kwargs

# def add(*nums):
#     print(sum(nums))

# add(10, 20, 30, 40, 50, 60)

# def bill(**products):
#     total = 0
#     for key, value in products.items():
#         print(key, value)
#         total += value
#     return f"Total amount is: {total}" 

# print(bill(tomato=20, potato=30, book=200))


# add = lambda num1, num2: num1 + num2
# print(add(10, 20))

nums = [1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda num:num**2, [1,2,3,4,5,6,7,8,9,10])))

# print(list(filter(lambda num:num%2==0,[1,2,3,4,5,6,7,8,9,10])
# print(list(filter(lambda num:num%2!=0,[1,2,3,4,5,6,7,8,9,10])

# local-global

# num = 20 # global var
# def test():
#     global num  # accessing global var from local scope
#     num = 10 # local var
#     print(num)

# test()
# print(num)

# num = 10
# num = 20

# print(num)


# nested functions

# def outer_func():
#     print("outer function")
#     def inner_func():
#         print("inner function")
#     inner_func()


# outer_func()


# decorators
# def capFunc(func):
#     def wrapper():
#         res = func().capitalize()
#         print("capitalize: ", res)
#         return res
#     return wrapper

# def titleFunc(func):
#     def wrapper():
#         res = func().title()
#         return res
#     return wrapper

# @titleFunc
# @capFunc
# def test():
#     return input("Enter something: ")

# print(test())


# def nums():
#     yield 1
#     yield 2
#     yield 3
#     for i in range(4, 11):
#         yield i

# num = nums()
# print(type(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))