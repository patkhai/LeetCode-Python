import random

mylist = [1, 4, 5, 8, 20, 18, 17, 11, 21, 22,
          40, 39, 44, 46, 50, 49, 54, 59, 51, 61, 63, 36, 37, 51, 53]

last = [1, 4, 5, 8, 20, 18, 17, 11, 21, 22]
x = random.sample(mylist, 5)
y = random.sample(last, 1)
print(x, y)
