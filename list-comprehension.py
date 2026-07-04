[expression for item in iterable if condition]
#     ↑            ↑                  ↑
# what to keep   loop var        optional filter

# Traditional loop
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# List comprehension ✅
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]


#List comprehension vs MAP/Filter:
numbers = [1, 2, 3, 4, 5]

# Using map + filter
result = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))

# Using list comprehension ✅ (cleaner)
result = [x**2 for x in numbers if x % 2 != 0]

print(result)  # [1, 9, 25]

#Calling a function:
def double(x):
    return x * 2

result = [double(x) for x in range(1, 6)]
print(result)  # [2, 4, 6, 8, 10]
