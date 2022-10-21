# -----------------------------------------------------------------------------
# -- Python Course => Strings => 01. Create, link and duplicate text strings --
# -----------------------------------------------------------------------------
stringOne = "This is string one"
stringTwo = "This is string Two"

print(stringOne)
print(stringTwo)

stringThree = "This is string \"Three\""

print(stringThree)

stringFour = "This is string 'Four'"

print(stringFour)

stringFive = 'This is string "Five"'

print(stringFive)

numbers = "1\n2\n3"

print(numbers)

numbers = """1
2
3"""
    
print(numbers)

# Concatenation
print(stringOne + stringTwo)
print(stringOne +" "+ stringTwo)

print(stringOne + str(10))

# Repeat
print("#" * 20)