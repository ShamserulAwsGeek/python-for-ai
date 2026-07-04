# map() — Transform each element
# map applies a function to every element and returns a new iterable.
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]


# filter() — Keep elements that match a condition
# filter keeps only elements where the function returns True.
numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]


# reduce() — Collapse elements into a single value
# reduce repeatedly applies a function to accumulate a result. 
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda acc, x: acc + x, numbers)
print(total)  # 15
