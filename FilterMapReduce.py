from functools import reduce

nums = [3, 2, 6, 8, 4, 6, 2, 9]

"""Filter"""

evens = list(filter(lambda n : n%2 == 0, nums))
print(evens)

"""Map"""

doubles = list(map(lambda n : n * 2, evens))
print(doubles)

"""Reduce"""

sum = reduce(lambda a,b  : a + b, doubles)
print(sum)
