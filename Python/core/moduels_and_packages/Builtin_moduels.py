import math

# print(dir(math))

# print(math.factorial(5))
# print(math.sqrt(25))
# print(math.sin(90))
# print(math.tan(45))

# import time
# while(True):
#     print("Tops")
#     time.sleep(2)

import random

# print(random.random())
# print(random.randint(1111, 9999))

# musics = [
#     "song1",
#     "song2",
#     "song3",
#     "song4",
#     "song5"
# ]
# random.shuffle(musics)
# print(musics)

# print(random.randrange(1,11,2))


from datetime import datetime, timedelta

current_time = datetime.now()

# print(current_time)
# print(current_time.date())
# print(current_time.day)
# print(current_time.month)
# print(current_time.year)
# print(current_time.time())
# print(current_time.hour)
# print(current_time.minute)
# print(current_time.second)
# print(current_time.microsecond)

# print(current_time + timedelta(days=1, hours=2))
# print(current_time - timedelta(days=1, hours=2))

current_time = datetime.now()

print(current_time.strftime('%d/%m/%Y, %I:%M:%S %p - %a %A'))

# https://docs.python.org/3/library/datetime.html