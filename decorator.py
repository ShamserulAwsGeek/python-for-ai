# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# print(myfunction())


def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Maheen"

@changecase
def otherfunction():
  return "I am Sham!"

print(myfunction())
print(otherfunction())