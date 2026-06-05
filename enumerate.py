# Definition and Usage
# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.

# The enumerate() function adds a counter as the key of the enumerate object.


marks = [12, 34,56,3,56,45,4]
for index, mark in enumerate(marks):
  print(mark)
  if(index ==3):
    print("Sham is awesoem!")


x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(type(y))

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
print(type(fruits))

for index,fruit in enumerate(fruits,start=1):
  print(index,fruit)
