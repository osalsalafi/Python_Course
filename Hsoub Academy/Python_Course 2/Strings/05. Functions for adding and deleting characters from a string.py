# ------------------------------------------------------------------------------------------------
# -- Python Course => Strings => 05. Functions for adding and deleting characters from a string --
# ------------------------------------------------------------------------------------------------

# startwith, endwith
stringOne = "This is string one"
print(stringOne.startswith("h"))
print(stringOne.startswith("This"))
print(stringOne.endswith("string one"))
print(stringOne.endswith("e"))
print(stringOne.endswith("E"))
print(stringOne.endswith("e",7,18))

print("#----------------------------------------------------#")
# strip, rstrip, lstrip
stringTwo = "    This is string Two    "
print(stringTwo)              #    This is string Two
print(stringTwo.strip())      #This is string Two
print(stringTwo.rstrip())     #    This is string Two
print(stringTwo.lstrip())     #This is string Two

stringThree = "@@@This is string three@@"
print(stringThree)              #@@@This is string three@@
print(stringThree.strip("@"))   #This is string three
print(stringThree.rstrip("@"))  #@@@This is string three

print("#----------------------------------------------------#")
# zfill
hours = "1"
minutes = "9"
seconds = "5"
print(f"{hours}:{minutes}:{seconds}")                             #1:9:5
print(f"{hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}")  #01:09:05

print("#----------------------------------------------------#")
hours = "1"
minutes = "9"
seconds = "25"
print(f"{hours}:{minutes}:{seconds}")                             #1:19:25
print(f"{hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}")  #01:09:25
