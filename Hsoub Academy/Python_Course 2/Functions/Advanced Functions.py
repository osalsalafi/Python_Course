# ----------------------------------------------------------------------
# -- Python Course => Lists and Dictionaries => 00. Advance Functions --
# ----------------------------------------------------------------------

# Argument unpacking
def info (name1, name2, name3) :
    print(f"First name is {name1}")
    print(f"Second name is {name2}")
    print(f"Third name is {name3}")

names = 'Ahmed', 'Khaled', 'Osama' # tuples
info(*names) #Asterisk

# Argument packing & unpacking
def info2 (*names1) :
    print(names1) # ('Ahmed', 'Khaled', 'Osama')     
    print(type(names1)) # <class 'tuple'>
    print(f"First name is {names1[0]}")
    print(f"Second name is {names1[1]}")
    print(f"Third name is {names1[2]}")

names0 = ['Ahmed', 'Khaled', 'Osama']
info2(*names0)

# Argument Dictionart Packing
def info3 (**kwargs):
    print(kwargs) # {'name': 'Osama', 'age': 26} 
    print(type(kwargs)) #<class 'dict'>
    print(f'My name is {kwargs["name"]}') # My name is Osama

info3(name="Osama", age=26) # it must be key arguments

# Argument Dictionart unPacking
def info4 (**kwargs) :
    print(f'My name is {kwargs["name"]} and my age is {kwargs["age"]}')
    # My name is Osama and my age is 26
infos = {'name' : 'Osama', 'age' : 26}
info4(**infos)

def foo(*args):
    print(args)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
foo(*l1, *l2)


