# open(filename, mode)

filename = 'example.txt'

# create file
# file = open(filename, 'w')
# file = open(filename, 'x')
# file = open(filename, 'a')

# file = open(filename, 'w')
# file.write("this is a write mode")
# file.close()
# file.write("again kuch write")

# file = open(filename, 'r')
# print(file.read())
# print(file.read(7))
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines())
# file.close()

file = open(filename, 'a')
# lines = ['\nThis is a line - 6\n', 'This is a line - 7\n', 'This is a line - 8\n', 'This is a line - 9\n', 'This is a line - 10']

# file.writelines(lines)

# print(file.tell())

# file.seek(0)

# print(file.tell())

import os

# os.system('git --version')
# os.system('mkdir test')

# os.system('type nul > test/main.txt')
# os.remove('test\\main.txt')
import uuid
# os.rename('sample.txt', f'{str(uuid.uuid4())}.txt')

# for num in range(1, 11):
#     os.system(f'type nul > {uuid.uuid4()}.xlsx')


# for file in os.listdir('test'):
#     if file.endswith('.pdf'):
#         os.remove(f'test\\{file}')