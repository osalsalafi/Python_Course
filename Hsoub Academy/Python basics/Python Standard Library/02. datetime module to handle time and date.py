# -------------------------------------------------
# -- 02. datetime module to handle time and date --
# -------------------------------------------------
# link : https://wiki.hsoub.com/Python/datetime
# from datetime import timedelta, tzinfo, time, date
# # two child classes that inherit from 
# # tzinfo >>
# from datetime import timezone
# # date, time
# from datetime import datetime
# # date, time, datetime, timezone are immutable 

print("#----------------------------------#")
from ctypes.wintypes import WORD
from datetime import date
world_cup_2022 = date(2022, 11, 21)
print(world_cup_2022)
# to reach the attributes of the class 
print(world_cup_2022.year)
print(world_cup_2022.month)
print(world_cup_2022.day)
# to get the date of today
today = date.today()
print(today)
# from ordinal 
some_day = date.fromordinal(738480) # by using the number of the day since the begining of the calender
print(some_day)
#YYYY-MM-DD
another_day = date.fromisoformat("2022-11-21")
print(another_day)
# get the remaining day for the 2022 world cup
days_to_world_cup_2022 = world_cup_2022 - today
print(days_to_world_cup_2022) # 37 days, 0:00:00 >> as timedelta
# to be printed as strings
print(type(world_cup_2022.isoformat())) #str
print(world_cup_2022.isoformat()) #2022-11-21
print(type(world_cup_2022.strftime("%a"))) #str
print(world_cup_2022.strftime("%a")) #Mon

print("#----------------------------------#")
from datetime import time
world_cup_2022_time = time(15,20,00) # the arguements here are choosen to be added or not
print(world_cup_2022_time)
# to reach the attributes of the class 
print(world_cup_2022_time.hour)
print(world_cup_2022_time.minute)
print(world_cup_2022_time.second)
time1 = time()
print(time1)
# from isoformat HH:MM:SS
time2 = time.fromisoformat("15:14:59")
print(time2)
# to be printed as strings
print(type(time2.isoformat()))
print(time2.isoformat())
print(time2.strftime("%I")) #3

print("#----------------------------------#")
from datetime import datetime
worldcup2022 = datetime(year=2022,month=11,day=21,hour=13, minute=0, second=0)
print(worldcup2022) # 2022-11-21 13:00:00
# to get the current date and time 
now = datetime.now()
print(now) #2022-10-15 16:47:52.175110
# now or today
now = datetime.today()
print(now)
# YYYY-MM-DD HH:MM:SS
newdatetime = datetime.fromisoformat("2022-11-21 14:40:00")
print(newdatetime)

countdown = now - worldcup2022
print("Countdown : ", countdown)

print("#----------------------------------#")
# timedelta is the space of two timezones
from datetime import timedelta
delta = timedelta(days=90, seconds=39, minutes=55, hours=4, weeks=0)
print(delta)

from datetime import datetime
now = datetime.now()

print(now + delta)

print("#----------------------------------#")
# tzinfo
# timezone


# strptime(d, '%') : from % to YYYY/MM/DD HH:MM:SS format
# strftime('%') : from YYYY/MM/DD HH:MM:SS to % format

# fromisoformat : from string to datetime.datetime format but must be in correct format
# isoformat : from datetime.datetime to string format in correct format