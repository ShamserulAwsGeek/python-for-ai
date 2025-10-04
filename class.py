# #Create a class with name myclass and a variable x with value 4:
# class myclass():
#     x =4
# #Create an object p1 of myclass and print the value of x:
# p1 = myclass()
# print(p1.x)


#Create a class named Person, use the __init__() method to assign values for name and age:
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# class shams:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# l1 = shams("Maheen", 25)
# print(l1.name)
# print(l1.age)

#The string representation of an object WITHOUT the __str__() method:
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1)


#The string representation of an object WITH the __str__() method:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name}({self.age})"

# p1 = Person("Sham", 29)
# print(p1)

#Insert a function that prints a greeting, and execute it on the p1 object:
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print("Hello my name is " + self.name)
#         print("My age is " + str(self.age))
    
# p1 = Person("Shams", 29)
# p1.myfunc()


#Use the words mysillyobject and abc instead of self:
# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#     print("My age is " + str(abc.age))

# p1 = Person("Shams", 29)
# p1.age = 30
# p1.myfunc()






