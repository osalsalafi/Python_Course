# ----------------------------------------------------------
# -- Python Course => Lists and Dictionaries => 01. Lists --
# ----------------------------------------------------------

employees = ['Ahmed', 'Osama', 'khaled', 'Ali']
print(employees) #['Ahmed', 'Osama', 'khaled', 'Ali']
print(employees[0])#Ahmed
print(employees[2])#khaled
print(employees[3])#Ali
print(employees[-1])#Ali
print(employees[0:2]) #['Ahmed', 'Osama']
print(employees[0:3:2]) #['Ahmed', 'khaled']
# it can be edited not like the tuples
employees[0] = 'Sara'
print(employees) #['Sara', 'Osama', 'khaled', 'Ali']

employees[:2] = 'Taj','Rami'
print(employees) #['Taj', 'Rami', 'khaled', 'Ali']
employees[:2] = ''
print(employees) #['khaled', 'Ali']

print("#---------------------------------------------#")
for index in employees :
    print(index)
    #khaled
    #Ali
for index in range(len(employees)):
    print(employees[index])
    #khaled
    #Ali

print("#---------------------------------------------#")
#enumerate
employees = ['Ahmed', 'Osama', 'khaled', 'Ali']
for index, item in enumerate(employees) :
    print(f"The employee number {index+1} in the list is : {item}")

print("#---------------------------------------------#")
# in or not in
print('Osama' in employees)
print('Osama' not in employees)
print('Rami' in employees)

print("#---------------------------------------------#")
# random.choice & random.shuffle
import random
employees = ['Ahmed', 'Osama', 'khaled', 'Ali']
print(random.choice(employees)) # to choice one item randomly
random.shuffle(employees) # to mix the items randomly
print(employees)