# ------------------------------------------------------------------
# -- Python Course => Strings => 08. Find and replace in a string --
# ------------------------------------------------------------------

# index (substring, start, end)
stringOne = "Hello world"
print(stringOne.index("world")) #6
print(stringOne.index("o")) #4
# print(stringOne.index("world", 0, 5)) #ValueError: substring not found

try :
    print(stringOne.index("world", 0, 5))
except ValueError :
    print("-1")

print("#----------------------------------------#")
# find(substring, start, end) , rfind
print(stringOne.find("world")) #6
print(stringOne.find("o")) #4
print(stringOne.rfind("o")) #7
print(stringOne.find("world", 0, 5)) #-1

print("#----------------------------------------#")
# replace(OldValue, NewValue, count)
stringTwo = "one plus one equal two"
print(stringTwo.replace("one","1"))
print(stringTwo.replace("one","1", 1))