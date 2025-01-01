# https://docs.python.org/3/library/re.html

import re

data = "hjdsfli ,mbdsc uiascmlui oijdf;,x.  jhc 12-23-1996 x.jkzch. hjikm .km x.ck 2-1-2024 kludyklds yubnpsfin,mfyhlk ufcd cuih 1/02/2025 jyhtgkjhdsljis jhufljsd ljuhlfds fkiuhf;ds 30/9-2022 jkdgfsyhkdhlisfjuisdh;lfsdjljui"

# pattern = r"\b\d{2}-\d{2}-\d{4}\b"
# pattern = r"\b\d{1,2}-\d{1,2}-\d{4}\b"
# pattern = r"\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b"
# res =  re.findall(pattern, data)
# print(res)

# data = "man mage more mm m mmmm mmm moon mind match maintain apple guava graps map mood"
# pattern = r'\bm\w*\b'
# pattern = r'\bm.*\b'
# pattern = r'\bm\w*\b'
# pattern = r'\bm\w{1,4}\b'
# res = re.findall(pattern, data)
# print(res)
# print(res.group())

# data = "This is a test string with some numbers 123, 456, 789, 000. And some words: apple, banana, orange, grapefruit, kiwi"
# pattern = r'\b\d{3},\d{3},\d{3}\b'
# res = re.findall(pattern, data)
# print(res)

# check mobile with proper format

# data = "9876543210, +91-9876543210, 09876543210, 987654321, +91 9876543210, +91-987654321, 0987654321, 98765432101234567890"
# pattern = r'\+?\d{1,3}[-.\s]?\d{10}\b'
# res = re.findall(pattern, data)
# print(res)

# sub:

data = "the kumbhmela conduct in suart."
# res = re.sub("suart", "pryagraj", data)
# print(res)

# res = re.split('\s', data)
# print(res)

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)

# fruits_with_price = [
#     ("apple", 100),
#     ("banana", 50),
#     ("orange", 150),
#     ("grapefruit", 200),
#     ("kiwi", 75)
# ]

# fruits = ''
# for fruit in fruits_with_price:
#     fruits += f" {fruit[0]}-{fruit[1]} "

# print(fruits)

# pattern = r'\b\w+-\d+\b'

# res = re.findall(pattern, fruits)

# print(res)
