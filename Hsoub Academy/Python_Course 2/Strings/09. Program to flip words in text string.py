# --------------------------------------------------------------------------
# -- Python Course => Strings => 09. Program to flip words in text string --
# --------------------------------------------------------------------------

# Try to do this application
# flip the words in the sentence to be as you are how hello
stringOne = "hello how are you"
list = stringOne.split(" ")
x = len(list)
list2 = []
print(list)
for index in list :
    list2.append(list[x-1])
    x -= 1

print(" ".join(list2))
# or
stringTwo = "hello how are you"
list = stringOne.split(" ")

list.reverse()
print(" ".join(list))