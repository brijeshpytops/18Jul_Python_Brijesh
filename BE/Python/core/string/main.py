"""
what is string in python?

A string is a sequence of characters. In Python, strings are immutable, meaning they cannot be changed after they are created.

"""

# syntax:

# string_name = "Hello, World!"
# string_name = 'Hello, World!'
# string_name = '''Hello, World!'''
string_name = """Hello, World!"""
# print(type(string_name))

# name = "python tech"
# print(len(name))


# Access elements of the string:

name = "python"

# print(name)

# indexing (+/-)

# print(name[0]) # p
# print(name[-3]) # h

# slicing (start:stop-1:step-1) (+/-)

# print(name[:])

# print(name[1:])

# print(name[:3])

# print(name[1:4])

# concat

# fname = "brijesh"
# lname = "gondaliya"
# fullname = fname + " " + lname
# print(fullname)

#replica
# star = "*"
# print(star*4)

# escape sequence
# print("brijesh gondaliya")
# print("\tbrijesh go\ndaliya")
# print(r"\tbrijesh go\ndaliya")

# sentance = "my name is \"brijesh gondaliya\""
# sentance = "my name is \'brijesh gondaliya\'"

# sentance = "\\\\"
# print(sentance)


# string methods:
# print(dir(''))

# name = "ToPs TEChNoLoGY Pvt. LTd."
# print(name.lower())
# print(name.upper())
# print(name.capitalize())
# print(name.title())
# print(name.swapcase())

name = "python programming"

# print(name.startswith("py"))

# print(name.endswith("on"))

# print(name.find("th"))

# print(name.index("th"))

# print(name.replace("th", "Th"))

# print(name.count("t"))

# print(name.split(" "))

# print(name.split("p"))

# print(input("Enter a something: ").split("p"))

# password = "testtyetwuT4#"
# u = 0
# l = 0
# s = 0
# d = 0

# if len(password) >= 8:
#     for ch in password:
#         if ch.isupper():
#             u = 1
#         elif ch.islower():
#             l = 1
#         elif ch.isdigit():
#             d = 1
#         elif not ch.isalnum():
#             s = 1
# else:
#     print("Password should be at least 8 characters long.")

# if u and l and s and d:
#     print("Valid password.")
# else:
#     print("Invalid password.")


center = "star"
# print(center.center(50, '-'))

# print(center.ljust(50, '-'))

# print(center.rjust(50, '-'))

# print(center.zfill(10))

# name = "     python tech     "

# print(name.strip())

# print(name.lstrip())
# print(name.rstrip())


# string formating
# import random
# mobile = "8980145007"
# price = 34.5454
# otp = random.randint(111111, 999999)
# otp_message = f"Your OTP is {otp}.\n\nPlease do not share this OTP with anyone."
# otp_message = "Your OTP is {}.\n\nPlease do not share this OTP with anyone.".format(otp)

# otp_message = "Your OTP is {}.\n\nPlease do not share this OTP with anyone. Contact us at {} or visit our website for more information or price {} for reachagre.".format(otp, mobile, price)
# otp_message = "Your OTP is {1}.\n\nPlease do not share this OTP with anyone. Contact us at {0} or visit our website for more information or price {2} for reachagre.".format(otp, mobile, price)
# otp_message = "Your OTP is %d.\n\nPlease do not share this OTP with anyone. Contact us at %s or visit our website for more information or price %.2f for reachagre."%(otp, mobile, price)
# print(otp_message)




