# -----------------------------------------------------------------------
# -- Python Course => Lists and Dictionaries => 05. List comperhension --
# -----------------------------------------------------------------------

numbers = [2,4,6,8,10]

new_numbers = [num*2 for num in numbers]
print(new_numbers) # [4, 8, 12, 16, 20]

new_numbers2 = [num*2 for num in numbers if num > 6]
print(new_numbers2) # [16, 20]