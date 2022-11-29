# --------------------------------------------------------------------------------------------------------
# -- Python Course => Regular Expressions => 06. Replacing and trimming texts through unit functions re --
# --------------------------------------------------------------------------------------------------------
import re

# Sub
txt = 'My name is Osama'

replace = re.sub(r'\s',r'-',txt)
print(replace) # My-name-is-Osama

replace = re.sub(r'\s',r'-',txt, 1)
print(replace) #My-name is Osama

replace = re.sub(r'\s',r'-',txt, 0)
print(replace) # My-name-is-Osama

# -----------------------------------------------------------------------

# split

text = 'My name is Osama'

seperate = re.split(r' ', text)
print(seperate) # ['My', 'name', 'is', 'Osama']

seperate = re.split(r'is', text)
print(seperate) # ['My name ', ' Osama']

seperate = text.split(' ')
print(seperate) # ['My', 'name', 'is', 'Osama']