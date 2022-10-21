# Finding the absolute value
num = -100
print(abs(num))
print("#-------------------------#")
# Round the number
num = 3.657
print(round(num)) # 4
print(round(num,1)) # 3.7
print(round(num,2)) # 3.66
print("#-------------------------#")
# Power to
num = 3
print(pow(num,2))
print("#-------------------------#")
# Finding the largest and smallest value
num = [100,200,300,400,500,600]
print(min(num))
print(max(num))
print("#-------------------------#")
# Add a set of numbers
num = [100,200,300,400,500,600]
print(sum(num))
print("#--------------------------#")
# Finding the square root using math library
import math
from msilib.schema import RemoveIniFile
num = 9
print(math.sqrt(num))
print("#--------------------------#")
# remainder of the division
from math import remainder
print(remainder(9,3)) # 0.0
print("#--------------------------#")
# Finding a random number
# generate a random number between 0-100
import random
print(random.randint(0,100)) #18
print("#--------------------------#")
# Create a date
import datetime
date = datetime.date(2021, 11, 10)
print(date) # 2021-11-10
print(date.year) # 2021
print(date.today()) # 2022-10-15
print("#--------------------------#")
# Create time
time = datetime.time(9,5,10)
print(time) # 09:05:10
print(time.minute) # 5
print("#--------------------------#")
# Find out the current time
now = datetime.datetime.today()
print(now) # 2022-10-15 13:42:11.636002
print(now.year)
print(now.day)
print("#--------------------------#")
# Convert date to text
date = datetime.date(2022, 10, 15)
time = datetime.time(8, 48, 20)
print(date)
print(time)
# put the format
print(date.strftime('%a')) # Sat
print(date.strftime('%A')) # Saturday
print(date.strftime('%w')) # 6 >> day in week
print(date.strftime('%d')) # 15 >> day in month
print(date.strftime('%j')) # 288 >> day in year
print(date.strftime('%b')) # Oct
print(date.strftime('%B')) # October
print(date.strftime('%m')) # 10
print(date.strftime('%y')) # 22
print(date.strftime('%Y')) # 2022
print(time.strftime('%H')) # 08 >> 24 hours
print(time.strftime('%I')) # 08 >> 12 hours
print(time.strftime('%p')) # AM 
print(time.strftime('%M')) # 48 >> Minutes
print(time.strftime('%S')) # 20 >> Seconds
print(time.strftime('%f')) # 000000 >> microseconds
