# -----------------------------------------------------------------------
# -- Python Course => Lists and Dictionaries => 06. Dictionary methods --
# -----------------------------------------------------------------------

# get
Osama = {
    'name' : 'Osama Alsalafi',
    # 'salary' : '6500',
    'number' : '0591403283',
    'skills' : ['HTML', 'CSS', 'Python']
}

# print(f"{Osama['name']} is getting {Osama['salary']}")
# Osama Alsalafi is getting 6500

print(f"{Osama['name']} is getting {Osama.get('salary', 'no salary')}")
# Osama Alsalafi is getting no salary

print("#------------------------------#")
# setdefault
print(Osama)
print(Osama.setdefault('languages', ['Arabic', 'English']))
print(Osama) # {'name': 'Osama Alsalafi', 'number': '0591403283', 'skills': ['HTML', 'CSS', 'Python'], 'languages': ['Arabic', 'English']}

print("#------------------------------#")
# update
Osama = {
    'name' : 'Osama Alsalafi',
    'salary' : '6500',
    'number' : '0591403283',
    'skills' : ['HTML', 'CSS', 'Python']
}
Osama['salary'] = 8500
print(Osama['salary'])
Osama.update({'salary':9000})
print(Osama['salary'])
Osama.update({'transportation':1350})
print(Osama)

print("#------------------------------#")
# clear
Osama.clear()
print(Osama) # {}

# for more methods :
# https://wiki.hsoub.com/Python/dict#.D8.A7.D9.84.D8.AF.D9.88.D8.A7.D9.84_.D8.A7.D9.84.D8.AA.D8.A7.D8.A8.D8.B9.D8.A9_.D9.84.D9.84.D9.83.D8.A7.D8.A6.D9.86_dict
