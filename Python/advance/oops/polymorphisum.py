# polymorphism
#     - method overloading
#           - compile time poly. - static binding
#     - method overriding
#           - runtime poly. - dynamic binding

# class Math1:
#     def add(self, a, b):
#         return a + b
    
#     def add(self, a, b, c):
#         return a + b + c
    
# obj = Math1()
# print(obj.add(1, 2, 3))

# class Math:
#     def add(self, a=None, b=None, c=None):
#         if a != None and b != None and c != None:
#             return a + b + c
#         elif a!=None and  b!=None:
#             return a+b

# obj = Math()

# print(obj.add(1, 2))
# print(obj.add(1, 2, 3))


# class Math1:
#     def display(self):
#         print("I am form parent class")

# class Math2(Math1):
#     def display(self):
#         super().display()  # calling parent class method
#         # print("I am form child class")

# obj = Math2()

# obj.display()