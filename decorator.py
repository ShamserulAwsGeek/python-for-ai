#A decorator is a function that wraps another function to extend or 
#modify its behavior — without changing the original function's code.
def greet(fx):
    def mfx(*args, **kwargs):
        print("Hello!")
        return fx(*args, **kwargs)
    return mfx

@greet
def hello():
    print("Welcome to the Python lab.")

@greet
def add(a, b):
    print(f"The sum of {a} and {b} is {a + b}")

hello()
add(5, 3)
------------------------------------
------------------------------------
#Another example of decorator:
def greater_first(func):
    def wrapper(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return wrapper

@greater_first
def divide(a, b):
    return a / b

@greater_first
def sub(a, b):
    return a - b

result1 = divide(2, 20)
result2 = sub(2, 20)

print(result1)
print(result2)

------------------------------------
------------------------------------
###Another examples of decorators:
def greater_first(func):
    def wrapper(*args, **kwargs):
        a,b = args[0], args[1]
        if a < b:
            a, b = b, a
        return func(a, b, *args[2:], **kwargs)
    return wrapper

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("values", args, " ", kwargs)
        result = func(*args, **kwargs)  
        print("result", result)
        return result
    return wrapper

@log_decorator
@greater_first
def divide(a, b):
    return a / b

@log_decorator
@greater_first
def sub(a, b):
    return a - b

@log_decorator
def add(a, b, c):
    return a + b + c


result1 = divide(2, 20)
print("result1", result1)

result2 = sub(10, 15)
print("result2", result2)

result3 = add(5, 3, 2)
print("result3", result3)









# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# print(myfunction())


# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Maheen"

# @changecase
# def otherfunction():
#   return "I am Sham!"

# print(myfunction())
# print(otherfunction())


# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# @changecase
# def otherfunction():
#   return "I am speed!"

# print(myfunction())
# print(otherfunction())

# def changecase(func):
#   def myfunc():
#     return func().lower()
#   return myfunc

# @changecase
# def lowerfunction():
#   return "I AM BENGALI "

# @changecase
# def otherlowerfunction():
#   return "I AM FROM MALDA"

# print(lowerfunction())
# print(otherlowerfunction())


# def changecase(func):
#   def myinner(x):
#     return func(x).upper()
#   return myinner

# @changecase
# def myfunction(nam):
#   return "Hello " + nam

# print(myfunction("John"))


# def changecase(func):
#   def myinner(*args, **kwargs):
#     return func(*args, **kwargs).upper()
#   return myinner

# @changecase
# def myfunction(fnam):
#   return "first name " + fnam

# @changecase
# def otherfunction(lnam):
#   return "last name "  +  lnam

# print(myfunction("Sham"))
# print(otherfunction("Maheen"))


# def changecase(n):
#   def changecase(func):
#     def myinner():
#       if n == 1:
#         a = func().lower()
#       else:
#         a = func().upper()
#       return a
#     return myinner
#   return changecase

# @changecase(1)
# def myfunction():
#   return "Hello Linus"

# print(myfunction())


# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# def addgreeting(func):
#   def myinner():
#     return "Hello " + func() + " Have a good day!"
#   return myinner

# @changecase
# @addgreeting
# def myfunction():
#   return "Tobias"

# print(myfunction())

# def myfunction():
#   return "Have a great day!"

# print(myfunction.__name__)



# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Have a great day!"

# print(myfunction.__name__)

import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)
