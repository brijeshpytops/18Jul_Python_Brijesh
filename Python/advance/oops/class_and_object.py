"""
what is class and object in python?

A class is a blueprint for creating objects (also known as instances). An object is an instance of a class.

Syntax:

class ClassName:
    # class body

object_name = ClassName()
"""

# name = "brijesh"
# age = 28

# def run():
#     return "I can run"

# print(name)
# print(age)
# print(run())

# class Person:
#     # data member [attributes and properties]
#     name = "brijesh"
#     age = 28

#     # member function [methods or behavior]
#     def run(yoyo):
#         return "I can run"
    

# obj = Person() 
# print(obj.name)
# print(obj.age)
# print(obj.run())


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def run(self):
#         return "I can run"
    
# users = []
# while True:
#     obj = Person(input("Enter your name: "), int(input("Enter your age: ")))
#     user = {
#         'name':obj.name,
#         'age': obj.age,
#         'can_run': obj.run()  # we are calling the method here which will return the string "I can run" directly without storing it in a variable. So, we don't need to store it in a variable.
#     }
#     users.append(user)
#     print(users)
#     print(f"Name: {obj.name}, Age: {obj.age}, Can run: {obj.run()}")