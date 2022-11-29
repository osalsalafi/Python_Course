# -----------------------------------------------------------------
# -- Python Course => Lists and Dictionaries => 05. Dictionaries --
# -----------------------------------------------------------------

# names = ['Ahmed', 'Osama', 'Ali']
# salary = ['5500','6500','7500']
# number = ['0531081276', '0591403283', '0509602726']

# Dictionary
Osama = {
    'name' : 'Osama Alsalafi',
    'salary' : '6500',
    'number' : '0591403283',
    'skills' : ['HTML', 'CSS', 'Python']
}
print(Osama) # {'name': 'Osama Alsalafi', 'salary': '6500', 'number': '0591403283', 'skills': ['HTML', 'CSS', 'Python']}

print("#----------------------------------#")
print(Osama['number']) # 0591403283

print("#----------------------------------#")
names1 = ['Ahmed', 'Osama', 'Ali']
names2 = ['Osama', 'Ali', 'Ahmed']
print(names1==names2) # False
print(names1[0]) # Ahmed
print(names2[0]) # Osama

print("#----------------------------------#")
Osama1 = {'name' : 'Osama', 'salary' : '6500', 'number' : '0591403283'}
Osama2 = {'salary' : '6500', 'number' : '0591403283', 'name' : 'Osama'}
print(Osama1==Osama2) # True
print(Osama1['number']) # 0591403283
print(Osama2['number']) # 0591403283

print("#----------------------------------#")
# birthdays = {'Osama':'8/24', 'Wafaa':'2/18'}
# while True :
#     name = input('Enter a name : (blank to quite)')
#     if name == '' :
#         break
#     if name in birthdays :
#         print(f"{birthdays[name]} is the birthday of " + name)
#     else :
#         print('The name is not in the list')
#         bd = input('Enter the birthday for that person : ')
#         birthdays[name] = bd

print("#----------------------------------#")
Osama = {'name' : 'Osama', 'salary' : '6500', 'number' : '0591403283'}
print(Osama.keys()) # dict_keys(['name', 'salary', 'number'])
print(Osama.values()) # dict_values(['Osama', '6500', '0591403283'])
print(Osama.items()) # dict_items([('name', 'Osama'), ('salary', '6500'), ('number', '0591403283')])