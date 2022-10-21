# -------------------------------------------------------------
# -- Python Course => Strings => 04. Case handling functions --
# -------------------------------------------------------------

# upper
stringOne = "This is string One"
print(stringOne.upper())

print("#----------------------------------------------------#")
# lower
print(stringOne.lower())

print("#----------------------------------------------------#")
# to save the changes of the function
print(stringOne)
stringOne = stringOne.upper()
print(stringOne)

print("#----------------------------------------------------#")
# We need such functions in case of comparing an answer with condition with sensitive case letter
# print("How are you ? ")
# feelings = input()
# if feelings == "great" :
#     print("That sounds good")
# else :
#     print("I wish you a better day")
# # if the answer is great that is fine, but if it is "Great" it will not give the correct answerg
# print("How are you ? ")
# feelings = input()
# if feelings.lower() == "great" :
#     print("That sounds good")
# else :
#     print("I wish you a better day")

print("#----------------------------------------------------#")
# islower, isupper
stringTwo = "This is string Two"
print(stringTwo.islower())
stringTwo = stringTwo.lower()
print(stringTwo.islower())

print("#----------------------------------------------------#")
stringTwo = "This is string Two"
# title
print(stringTwo.title())
# This Is String Two

print("#----------------------------------------------------#")
# capitalize
print(stringTwo.capitalize())
# This is string two

print("#----------------------------------------------------#")
# swapcase
print(stringTwo.swapcase())
# tHIS IS STRING tWO

print("#----------------------------------------------------#")
# isalnum
print(stringTwo.isalnum()) #False
stringThree= "A548"
print(stringThree.isalnum()) #True

print("#----------------------------------------------------#")
# isdigit
print(stringThree.isdigit()) #False
stringFour = "1234"
print(stringFour.isdigit()) #True

print("#----------------------------------------------------#")
# isalpha
# isdecimal
# isidentifier
# isnumeric
# isspace
# istitle
