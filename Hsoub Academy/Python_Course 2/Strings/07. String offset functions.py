# -------------------------------------------------------------
# -- Python Course => Strings => 07. String offset functions --
# -------------------------------------------------------------

# rjust, ljust, center
stringOne = "Hello"
print(stringOne.rjust(10)) # 10 indexes including the letters of the world >> so it must be more that 5 here
print(stringOne.rjust(6))  # Hello
print(stringOne.center(18))

# we can use just with sign
print(stringOne.center(18,"-"))

print("#----------------------------------------------------#")

#expandtabs
stringFour = "Hello \tdear Osama,\t I hope that you are doing well"
print(stringFour.expandtabs(5))
print(stringFour.expandtabs(0))
print(stringFour.expandtabs(10))