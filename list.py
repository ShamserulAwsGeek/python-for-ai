# thislist = ["apple", "banana", "cherry", "apple"]
# print(len(thislist))


# mylist = ["Bangalore", "Chennai", "Mumbai", "Delhi"]
# print(type(mylist))

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-3])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.insert(3,"orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(len(thislist))
# print(type(thislist))

#list constructor:
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


# thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
# for x in thislist:
#   print(x)


# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])
# print(i)

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


# thislist = ["apple", "banana", "kiwi"]
# [print(x) for x in thislist]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)


# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)


# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
#print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = [4,5,6]
list4 =[7,8,9,10]

for x in list2:
  list1.append(x)
for y in list3:
  list1.append(y)

for z in list4:
  list1.append(z)

print(list1)

#List comprehension:
lst = [i for i in range(5)]
print(lst)
