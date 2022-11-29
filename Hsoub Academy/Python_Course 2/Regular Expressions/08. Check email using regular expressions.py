# ---------------------------------------------------------------------------------------
# -- Python Course => Regular Expressions => 08. Check email using regular expressions --
# ---------------------------------------------------------------------------------------
import re
# email = input('Pls enter your email : ')

# search = re.search(r'[A-Za-z0-9\._-]+@(gmail|mail|yahoo|hsoub)\.(com|net|edu)',email)

# if search :
#     print('Your email is valid')
# else :
#     print('Your email is not valid')


# another example

# email = 'os.alsalafi@fastnet.com'
# search = re.search(r'[A-Za-z0-9\._-]+@\w+\.\w{2,3}',email)
# if search :
#     print('Your email is valid')
# else :
#     print('Your email is not valid')

# another example : if we want it to starts and ends with the same expression only
# put ^ at the beginning and $ at the end

# email = 'os.alsalafi@fastnet.com'
# search = re.search(r'^[A-Za-z0-9]+[\._-]?[A-Za-z0-9]+@\w+\.\w{2,3}$',email)
# if search :
#     print('Your email is valid')
# else :
#     print('Your email is not valid')


# compile
email = 'os.alsalafi@fastnet.com'
search = re.compile(r'^[A-Za-z0-9]+[\._-]?[A-Za-z0-9]+@\w+\.\w{2,3}$')

if re.fullmatch(search,email) :
    print('Your email is valid')
else :
    print('Your email is not valid')
