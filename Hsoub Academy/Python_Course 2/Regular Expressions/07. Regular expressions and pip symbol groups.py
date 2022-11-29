# -------------------------------------------------------------------------------------------
# -- Python Course => Regular Expressions => 07. Regular expressions and pip symbol groups --
# -------------------------------------------------------------------------------------------

# Grouping
import re

number = '050-960-2726'

search = re.search(r'(\d{3})-(\d{3})-(\d{4})',number)

# print(search.group()) #050-960-2726
# print(search.group(0)) #050-960-2726
# print(search.group(1)) #050
# print(search.group(2)) #960
# print(search.group(3)) #2726

# + >> it means that at least we have one of this letter
txt = 'abbbbbabbbbbabbbbb'

search = re.search(r'ab+',txt)
print(search.group()) # abbbbb

search = re.search(r'(ab)+',txt)
print(search.group()) # ab

# | >> it means or 
txt1 = 'my name is ali, my name is ahmed'

search = re.search(r'my name is (osama|ahmed)',txt1)
print(search.group()) # my name is ahmed 

# ------------------- Practice -------------------------
date = '29-11-2022'
search = re.search(r'(\d{2})\-(\d{2})\-(\d{4})',date)
# day = search.group(1)
# month = search.group(2)
# year = search.group(3)

# print(f'today date is {day}, in month number {month}, in {year} year')
# today date is 29, in month number 11, in 2022 year


# in another way

day, month, year = search.groups()
print(f'today date is {day}, in month number {month}, in {year} year')
# today date is 29, in month number 11, in 2022 year
