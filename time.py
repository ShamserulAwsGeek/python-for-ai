#calculate live time
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

#Decide part of the day:
import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("enter the hour:"))
print(hour)

if(hour>=0 and hour<12):
  print("Good Morning!")

elif(hour>=12 and hour< 17):
  print("Good Evening!")

else:
  print("Good night!")
