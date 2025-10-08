# import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)

#Print a list of all matches:
# import re

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)

#Return an empty list if no match was found:
# import re

# txt = "The rain in Spain"
# x = re.findall("Portugal", txt)
# print(x)

#Search for the first white-space character in the string:
# import re

# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:", x.start())
# print(x)

#Make a search that returns no match:
# import re

# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)

#Split at each white-space character:
# import re

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)


#Split the string only at the first occurrence:
# import re

# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)


#Replace every white-space character with the number 9:
# import re

# txt = "sham loves Maheen"
# x = re.sub("\s", "Maheen", txt)
# print(x)

#Replace the first 2 occurrences:
# import re

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)

#Do a search that will return a Match Object:
# import re

# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x) #this will print an object

# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.span())


# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.string)

# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.group())