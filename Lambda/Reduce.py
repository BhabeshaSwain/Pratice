from functools import reduce

li = [1000, 2000, 3000, 4000, 5000]

data = reduce(lambda x, y: x + y, li)
print(data)
