from functools import reduce

numbers = list(range(1, 11))
result = reduce(lambda x, y: x + y, numbers)
print(result)