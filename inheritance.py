#Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()


class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2017

def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Shams", "Haque", 2017)
print(x.welcome())


---------------------------
-----------------------------

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id}")

class Programmer(Employee):
    def show_language(self, language):
        print("The default programming language is: Python")

e = Employee("John Doe", 12345)
e.display_info()
p = Programmer("Shamserul", 12346)
p.display_info()
p.show_language("Python")
