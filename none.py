#Assign and display a None value:
# x = None
# print(x)

#Assign and print the data type of a None value:
# x = None
# print(type(x))

#Use the identity operator is for comparisons with None:
# result = None
# if result is None:
#   print("No result yet")
# else:
#   print("Result is ready")

# result = None
# if result is not None:
#   print("Result is ready")
# else:
#   print("No result yet")

# print(bool(None))

#A function without a return statement returns None:
def myfunc():
  x = 5
  
x = myfunc()
print(x)