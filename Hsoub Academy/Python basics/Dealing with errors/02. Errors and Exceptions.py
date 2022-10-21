# ---------------------------
# -- Errors and Exceptions --
# ---------------------------

# SyntaxError
# print(3+2
# >> missing ')' in print to execute the programme

# NameError
# prin(3+2)
# >> missing 't' in print to execute the programme

# ZeroDivisionError
# print(3/0)

# ----------- print Error ----------- #
# raise Exception("This is an Exception") 


# ----------- try-except ------------ #
from decimal import DivisionByZero


try:
    x = 6
    y = 3
    print(x/(x-y))
except:
    print("Did you divide by 0 ?")

print("#--------------------------------#")
try:
    x = 3
    y = 3
    print(x/(x-y))
except:
    print("Did you divide by 0 ?")

print("#--------------------------------#")
# ----------- try-except with files ------------ #
# with open("my_file.txt") as file :
#     file.read()
# ------------- it can be in general for any mistake or specific -------#
# ------------- In general
try:
    with open("my_file.txt") as file :
        file.read()
except:
    print("File is not found")
# ------------- Specific
try:
    with open("my_file.txt") as file :
        file.read()
    # x = 3
    # y = 3
    # print(x/(x-y))
except FileNotFoundError as error :
    print(error)
except ZeroDivisionError as error :
    print(error)

# ------------- use else in try except
try:
    with open("text.txt",'w') as file :
        
        x = 6
        y = 3
        file.write(f"{x/(x-y)}")
except FileNotFoundError as error :
    print(error)
except ZeroDivisionError as error :
    print(error)
else : # in case there is no errors
    print("The result has been written to the file")
finally : # no matter what is the case
    print("The code has been executed")

# ------------- If the exception is not in python ------------- #
class TooOldError(Exception):
    def __str__(self):
        return f"Sorry, you can not sign in because you are too old."

class TooYoungError(Exception):
    def __str__(self):
        return f"Sorry, you can not sign in because you are too young."

age = int(input("Enter your age : "))
if age < 15 : raise TooYoungError
if age > 40 : raise TooOldError

print("#------------------------------------------------#")
class TooOldError1(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class TooYoungError1(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

age = int(input("Enter your age : "))
if age < 15 : raise TooYoungError1(f"Sorry, you age is {age}, so you can not sign in because you are too young.")
if age > 40 : raise TooOldError1(f"Sorry, you age is {age}, so you can not sign in because you are too old.")

