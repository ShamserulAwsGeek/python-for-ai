# # Empty list
# x = []
# print(x)

# # List with initial values
# y = [1, 2, 3, 4, 5]
# print(y)
# # List with mixed types
# z = [1, "hello", 3.14, True]
# print(z)

#Append one element to the list, and sort the list ascending:
# x = [9, 12, 7, 4, 11]

# # Add element:
# x.append(8)

# # Sort list ascending:
# x.sort()
# print(x)  

#Create an algorithm to find the lowest value in a list:
my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)