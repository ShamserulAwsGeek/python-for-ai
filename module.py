# def greeting(name):
#   print("Hello, " + name)

# import module

# module.greeting("ShamsMaheen")


# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }

# import module
# a = module.person1["age"]
# print(a)

# import module as mx
# a = mx.person1["age"]
# print(a)


# import platform
# x = platform.system()
# print(x)

#List all the defined names belonging to the platform module:
# import platform

# x = dir(platform)
# print(x)


def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

from module import person1
print(person1["country"])