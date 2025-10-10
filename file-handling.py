# f = open("sham.txt")
# print(f.read())

#Open a file on a different location:
# f = open("D:\\myfiles\welcome.txt")
# print(f.read())

#Using the with keyword:
# with open("sham.txt") as f:
#   print(f.read())

#Close the file when you are finished with it:
# f = open("sham.txt")
# print(f.readline())
# f.close()

#Return the 5 first characters of the file:
# with open("sham.txt") as f:
#   print(f.read(5))

# with open("sham.txt") as f:
#   print(f.read(10))

#Read one line of the file:
# with open("sham.txt") as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())

#Loop through the file line by line:
# with open("sham.txt") as f:
#   for x in f:
#     print(x)