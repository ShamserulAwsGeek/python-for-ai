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

#Open the file "sham.txt" and append content to the file:
# with open("sham.txt", "a") as f:
#   f.write("Now the file has more content!")

# #open and read the file after the appending:
# with open("sham.txt") as f:
#   print(f.read())

#Open the file "sham.txt" and overwrite the content:
# with open("sham.txt", "w") as f:
#   f.write("Woops! I have deleted the content!")

# #open and read the file after the overwriting:
# with open("sham.txt") as f:
#   print(f.read())

#Create a new file called "myfile.txt":
# f = open("myfile.txt", "x")

#Remove the file "myfile.txt":
# import os
# os.remove("myfile.txt")


#Check if file exists, then delete it:
# import os
# if os.path.exists("myfile.txt"):
#   os.remove("myfile.txt")
# else:
#   print("The file does not exist")

#To delete an entire folder, use the os.rmdir() method:
import os
os.rmdir("myfolder")

 #File Handling:

a = input("Enter num:")
print(f"multiplication table of {a} is:")

try:
  for i in range(1,11):
    print(f"{int(a)} x {i} = {int(a)*i}")

except:
  print('Invalid input')

print("some important line of codes")
print("End of program")
