# Filter

li = [11, 12, 13, 14, 15, 16]
data = list(filter(lambda x: x % 2 == 0, li))
print(data)

li = [10, 'BH', 20, 'SW']
data = list(filter(lambda i: isinstance(i, str), li))
print(data)
