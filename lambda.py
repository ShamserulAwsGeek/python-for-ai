# x = lambda a : a + 10
# print(x(5))


# x = lambda a, b : a * b
# print(x(5, 6))

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

# def myfunc(n):
#   return lambda a : a * n


# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# def myfunc(n):
#   return lambda a : a * n

# mytripler = myfunc(3)

# print(mytripler(11))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))



# Lambda Functions in Python
# A lambda function is a small, anonymous (nameless) function defined in a single line.

#syntax :  lambda arguments : expression

# Regular function
def add(x, y):
    return x + y

# Same thing as a lambda
add = lambda x, y: x + y
print(add(3, 4))   # 7


double = lambda x: x * 2
cube = lambda x: x ** 3
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))  # Output: 10
print(cube(3))    # Output: 27  
print(avg(4, 5, 6))  # Output: 5.0
