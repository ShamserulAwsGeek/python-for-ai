#Create an f-string:
# txt = f"The price is 49 dollars"
# print(txt)

#Add a placeholder for the price variable:
# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

#Display the price with 2 decimals:
# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

#Display the value 95 with 2 decimals:
# txt = f"The price is {95:.2f} dollars"
# print(txt)

#Perform a math operation in the placeholder, and return the result:
# txt = f"The price is {20 * 59} dollars"
# print(txt)

#Add taxes before displaying the price:
# price = 59
# tax = 0.25
# txt = f"The price is {price + (price * tax)} dollars"
# print(txt)

#Return "Expensive" if the price is over 50, otherwise return "Cheap":
# price = 49
# txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

# print(txt)

#use the string method upper()to convert a value into upper case letters:
# fruit = "maheen"
# txt = f"Sham loves {fruit.upper()}"
# print(txt)

#Create a function that converts feet into meters:
# def myconverter(x):
#   return x * 0.3048

# txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
# print(txt)

#Use a comma as a thousand separator:
# price = 59000
# txt = f"The price is {price:,} dollars"
# print(txt)

#Add a placeholder where you want to display the price:
# price = 49
# txt = "The price is {} dollars"
# print(txt.format(price))

#And add more placeholders:
# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

#Also, if you want to refer to the same value more than once, use the index number:
# age = 36
# name = "John"
# txt = "His name is {1}. {1} is {0} years old."
# print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))