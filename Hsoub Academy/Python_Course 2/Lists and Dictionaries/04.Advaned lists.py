# -------------------------------------------------------------------
# -- Python Course => Lists and Dictionaries => 04. Advanced lists --
# -------------------------------------------------------------------

#filter
ages = [10, 20 ,65, 2, 15 , 45, 13]

def filter_age(age):
    return age >= 18

print(filter(filter_age, ages)) # <filter object at 0x000002D00501ADD0>
print(list(filter(filter_age, ages))) # [20, 65, 45]

#map
numbers = [5, 10, 15, 20, 25]

def square(num) :
    return num ** 2

print(list(map(square,numbers))) # [25, 100, 225, 400, 625]