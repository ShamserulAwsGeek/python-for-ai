# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# thistuple = ("apple",)
# print(type(thistuple))

#NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))


# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-3])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")


# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)



# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# z= list(thistuple)

# y.append("orange")
# z.append("mango")

# thistuple = tuple(y)
# thistuple = tuple(z)
# print(thistuple)


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)

# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])

# thistuple = ("amma", "abba", "bahan")
# for i in range(len(thistuple)):
#     print(thistuple[i])
# print(i)


# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1
# print(i)

# thistuple = ("Ashriti", "Maheen", "Farah")
# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i = i +1
# print(i)    



# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)