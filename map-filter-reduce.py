#MAP:
# map() — Transform each element
# map applies a function to every element and returns a new iterable.
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

#another exapmles of Map:
def cube(x):
    return x ** 3
print(cube(3))  # Output: 27

num = [1, 2, 3, 4, 5]
cubed_numbers = list(map(cube, num))
print(cubed_numbers)  # Output: [1, 8, 27, 64, 125]

-----------------------------------------------

#Filter:
# filter() — Keep elements that match a condition
# filter keeps only elements where the function returns True.
numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]

#another example of Filter:
num = [1,2,3,4,5,6,7,8,9,10]

def filter_function(num):
    if num > 2:
        return True
    else:
        return False
    
filtered_num = list(filter(filter_function, num))
print(filtered_num)

------------------------------------------

#Reduce:

# reduce() — Collapse elements into a single value
# reduce repeatedly applies a function to accumulate a result. 
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda acc, x: acc + x, numbers)
print(total)  # 15


#Combined example:
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = reduce(
    lambda acc, x: acc + x,          # sum them up
    map(lambda x: x ** 2,            # square each
        filter(lambda x: x % 2 == 0, numbers))  # keep evens
)

print(result)  # 4 + 16 + 36 + 64 + 100 = 220


from functools import reduce

num = [1, 2, 3, 4, 5]

def mysum(x, y):
    return x + y
sum = reduce(mysum, num)
print(sum)
