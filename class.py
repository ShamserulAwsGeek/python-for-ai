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


#Static Method : static method is a method that belongs to the class itself, not to any instance (object) of the class.

class Math:
    def __init__(self,num):
        self.num = num


    def addtonum(self, n):
        self.num += n

    @staticmethod
    def add(x, y):
        return x + y
    
result = Math.add(5, 10)
print(result)  # Output: 15

a = Math(10)
print(a.num)  # Output: 10
a.addtonum(5)
print(a.num)  # Output: 15

#The core idea: if a method doesn't need self or cls, 
#it's a good candidate to be static. 
#It signals to readers "this doesn't touch object state" and can be called without creating an object.

class Example:
    
    class_var = 0

    def instance_method(self):      # Access instance (self) + class data
        return self

    @classmethod
    def class_method(cls):          # Access class (cls), not instance
        return cls.class_var

    @staticmethod
    def static_method():            # Access neither — fully independent
        return "I'm standalone"

---------------------------------------
---------------------------------------
#Instance Variable and Class Variable:
#Class Variable -- Shared across all instances of the class. Defined directly in the class body.the neighborhood name (same for every house built from that blueprint)
#Instance Variable ---Unique to each object. Defined inside __init__ using self.the house color (each house can be different)

class Employee:
    company_name = "Optum"
    no_of_employees = 0

    def __init__(self,name):
        self.name = name
        self.raise_amount = 1.04
        Employee.no_of_employees += 1
    
    def showDetails(self):
        print(f"Employee Name: {self.name} and the raise amount in {self.no_of_employees} sized  {self.company_name} is: {self.raise_amount}")

e1 = Employee("Shamserul")
e1.raise_amount = 2
e1.company_name = "Optum India"
e1.showDetails()
print(Employee.company_name)

e2 = Employee("Maheen")
e2.showDetails()

-----------------------------
------------------------------
class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)


    def showinfo(self):
        print(f"The library has  {self.no_of_books} books")
        for book in self.books:
            print(book)             
    
l1 = Library()
l1.add_book("Python Programming")
l1.add_book("Data Science")
l1.showinfo()
-----------------------------------
---------------------------------\
#Class Method: Class methods in Python are methods bound to the class itself rather than to an instance. 
#They receive the class (cls) as their first argument instead of self.

class Employee:
    company = "Optum"

    def show(self):
        print(f"My name is {self.name} and I work at company {self.company}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee()
e1.name = "Shmaserul"
e1.show()  # Output: My name is Shmaserul and I work at company Optum

e1.change_company("Illumina")
e1.show()  # Output: My name is Shmaserul and I work at company Illumina
print(Employee.company)  # Output: Illumina
