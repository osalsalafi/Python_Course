# ----------------------------------------------------------
# -- Python Course => Strings => 02. Indexing and Slicing --
# ----------------------------------------------------------
import string


stringOne = "This is string one"

# Indexing
print(stringOne[0])
print(stringOne[10])
print(len(stringOne))
print(stringOne[17]) # len - 1
print(stringOne[-1])
print(stringOne[-18])

print("#----------------------------------------------#")

# Slicing [start:end:step]

print(stringOne[7:10])
print(stringOne[:10])
print(stringOne[10:])
print(stringOne[1:10:2])
print(stringOne[-6:-18:-2])
print(stringOne[::-1])


print("#----------------------------------------------#")
# slice
name = "Osama Abdullah Mohammed Alsalafi"
print(name[0:6])
s = slice(0,6)
print(name[s]) #Osama


