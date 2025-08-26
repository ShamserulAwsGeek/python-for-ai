# x = 5
# y = "John"
# print(x)
# print(y)



# x = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(x)

#Casting:
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# x = 5
# y = "John"
# print(type(x))
# print(type(y))


# x = "John"
# # is the same as

# x = 'John'


#Variable names are case-sensitive:
# a = 4
# A = "Sally"
#A will not overwrite a

#Python allows you to assign values to multiple variables in one line:
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)


#Unpack a list:
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)


#you can assign the same value to multiple variables in one line:
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)


#output of variables:

# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)

#You can also use the + operator to output multiple variables:

# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# x = 5
# y = 10
# print(x + y)

# x = 5
# y = "John"
# print(x , y)


#Create a variable outside of a function, and use it inside the function:

# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()

#Create a variable inside a function, with the same name as the global variable:

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)