# ----------------------------------------------------------------------------------
# -- Python Course => Regular Expressions => 05. Search through unit functions re --
# ----------------------------------------------------------------------------------

import re

# ================================= Search ======================================= #

txt = 'My name is Osama'

new_search = re.search('[A-Z]', txt)

print(new_search) # <re.Match object; span=(0, 1), match='M'> >> only the first matched item found

# -------------------------------- #

txt = 'my Name is Osama'

new_search = re.search('[A-Z]', txt)

print(new_search) # <re.Match object; span=(3, 4), match='N'>

# -------------------------------- #

# txt = 'my name is osama'

# new_search = re.search('[A-Z]', txt)

# print(new_search) # None

# -------------------------------- #

# txt = 'My name is Osama'

# new_search = re.search('[A-Z]', txt)

# print(new_search)
# print(new_search.span()) # (0,1)
# print(dir(new_search))
# print(new_search.group()) # M

# -------------------------------- #

txt = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'

search = re.search(r"\d{3}-\d{3}-\d{4}",txt)
# print(search.group()) # 415-555-1011

# -------------- Check Phone Number ------------------ #
def check_phone_number(number):
    is_phone = re.search(r"[+]\d{3}\s\d{2}\s\d{3}\s\d{4}",number)

    if is_phone:
        print(f'The {number} is correct phone number')
    else :
        print(f'The {number} is not a phone number')

number = "+966 59 140 3283"
check_phone_number(number) # The +966 59 140 3283 is correct phone number 

# ================================= findall ======================================= #

txt = 'Call me at 415-555-10126 tomorrow. +966 59 140 3283 is my office'

search = re.findall(r"\d{3}-\d{3}-\d{4}",txt)

print(search) # ['415-555-1011', '415-555-9999'] >> it will return a list with all matched texts

search = re.findall(r"[+]\d{3}\s?\d{2}\s?\d{3}\s?\d{4}",txt)

print(search) # []

# ================================= Excercise ======================================= #
note_book = []
while True :
    number = input('Enter you number in this format +966 50 960 2726 : ')
    check_number = re.findall(r"[+]\d{3}\s?\d{2}\s?\d{3}\s?\d{4}",number)
    if check_number != []:
        note_book.extend(check_number)
        print('Your phone number is added')
        print("===========================")
        print(note_book)
        check_number = []
    else :
        print('The phone number is not valid, try again')
