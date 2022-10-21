# --------------------------------------------------------------------------------------------
# -- Python Course => Lists and Dictionaries => 03. Search, count, copy and erase functions --
# --------------------------------------------------------------------------------------------
# index 
employee = ['Hasan', 'Hadi', 'Reem', 'Ahmed']
print(employee.index("Ahmed")) #3
# print(employee.index("Sara"))

print("#-------------------------------------------#")
# count
print(employee.count('Ahmed')) #1

print("#-------------------------------------------#")
# copy
test = employee.copy()
print(test) #['Hasan', 'Hadi', 'Reem', 'Ahmed']

print("#-------------------------------------------#")
# clear
test.clear()
print(test) #[]

