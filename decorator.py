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

def changecase(func):
  def myfunc():
    return func().lower()
  return myfunc

@changecase
def lowerfunction():
  return "I AM BENGALI "

@changecase
def otherlowerfunction():
  return "I AM FROM MALDA"

print(lowerfunction())
print(otherlowerfunction())