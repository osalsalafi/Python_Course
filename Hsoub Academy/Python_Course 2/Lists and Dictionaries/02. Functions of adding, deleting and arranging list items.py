
# -----------------------------------------------------------------------------------------------------------
# -- Python Course => Lists and Dictionaries => 02. Functions of adding, deleting and arranging list items --
# -----------------------------------------------------------------------------------------------------------
# append and insert
employee = ['Hasan', 'Hadi', 'Reem', 'Ahmed']
employee.append('Osama')
employee.insert(2, 'Wafaa')
print(employee) #['Hasan', 'Hadi', 'Wafaa', 'Reem', 'Ahmed', 'Osama']
old_employees = ['Khaled', 'Bilal']
# employee.append(old_employees) # ['Hasan', 'Hadi', 'Wafaa', 'Reem', 'Ahmed', 'Osama', ['Khaled', 'Bilal']]
# print(employee)
# print(employee[6])
# but to extend them in the list directly

print("#-------------------------------------------#")
# extend
employee.extend(old_employees)
print(employee) # ['Hasan', 'Hadi', 'Wafaa', 'Reem', 'Ahmed', 'Osama', 'Khaled', 'Bilal'] 

print("#-------------------------------------------#")
# remove
employee.remove('Reem')
print(employee) # ['Hasan', 'Hadi', 'Wafaa', 'Ahmed', 'Osama', 'Khaled', 'Bilal']
# if I have two from the same names "remove" will remove one only 
 
print("#-------------------------------------------#")
# del statement
del employee[0] 
print(employee) #['Hadi', 'Wafaa', 'Ahmed', 'Osama', 'Khaled', 'Bilal']

print("#-------------------------------------------#")
# pop
employee.pop(0)
print(employee) #['Wafaa', 'Ahmed', 'Osama', 'Khaled', 'Bilal']

print("#-------------------------------------------#")
# sort
num = [1,5,9,3,1,7]
num.sort()
print(num) # [1, 1, 3, 5, 7, 9]
num.sort(reverse=True)
print(num) # [9, 7, 5, 3, 1, 1]
# list = [1,5,2,7, "Ahmed", "Osama"]
# list.sort() # it must be from the same data type

print("#-------------------------------------------#")
# reverse
employee.reverse()
print(employee) #['Bilal', 'Khaled', 'Osama', 'Ahmed', 'Wafaa'] 