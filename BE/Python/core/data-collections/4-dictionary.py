"""
Dictionary: oredered, mutable, duplictae keys are not allowed

syntax:

dictionary_name = {
    key1: value1,
    key2: value2,
    ...
    keyN: valueN
}

dictionary_name = dict()
"""

# dictionary_of_items = {
#     "name": "John", 
#     "age": 30, 
#     "city": "New York"
# }

# print(dictionary_of_items)
# print(dictionary_of_items['name'])
# print(dictionary_of_items['age'])
# print(dictionary_of_items['city'])

# contacts = [
#     {"name": "John", "phone": ["1234567890", "7847683567"]},
#     {"name": "Jane", "phone": "9876543210"},
#     {"name": "Bob", "phone": "0987654321"},
#     {"name": "Alice", "phone": "1234567890"}
# ]
# print(contacts[0]["phone"][1])

# methods

# car = {
#     "make": "Toyota",
#     "model": "Camry",
#     "year": 2020,
#     # "color":"red"
# }

# print(dir(car))

# print(car.get('make'))
# print(car.keys())
# print(car.values())

# keys = list(car.keys())
# values = list(car.values())
# print(list(zip(keys, values)))

# print(car.items())


# num1 = [1,2,3,4,5, 6]
# num2 = [11,22,33,44,55]
# num3 = [111,222,333,444,555]
# print(list(zip(num1, num2, num3)))


# car.pop('make')
# car.popitem()
# car.update({'color':"red"})
# car.setdefault("color", "blue")
# print(car)

# items = ['tomato', 'potato', 'onion']
# price = 50

# products = {}
# print(products.fromkeys(items, price))

# users = []

# flag = True
# while flag:
#     choice = input("Do you want to add another user? (yes/no): ")
#     if choice.lower() == 'no':
#         flag = False
#     else:
#         user = {}
#         user["name"] = input("Enter name: ")
#         user["age"] = int(input("Enter age: "))
#         users.append(user)
#         print(users)
        
      