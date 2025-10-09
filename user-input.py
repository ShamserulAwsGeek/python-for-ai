#Ask for user input:
# print("Enter your name:")
# name = input()
# print(f"Hello {name}")
# print("whom do you love?")
# love = input()
# print(f"{love} loves you too")

#Add a message in front of the user input:
# name = input("Enter your name:")
# print(f"I am  {name}")

#Multiple inputs:
# name = input("Enter your name:")
# print(f"Hello {name}")
# ques1 = input("Whom do you love:")
# ques2 = input("how much do you lover her:")
# ques3 = input("Does she love you:")
# print(f"Can you live without {ques1}, I love her {ques2} and {ques3} ?")

#To find the square root, the input has to be converted into a number:
# import math
# x = input("Enter a number:")

# #find the square root of the number:
# y = math.sqrt(float(x))

# print(f"The square root of {x} is {y}")

#Keep asking until you get a number:
y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x)
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")