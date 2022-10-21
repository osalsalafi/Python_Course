# -----------------------------------------------------------------------------
# -- Python Course => Strings => 06. String-binding and decoupling functions --
# -----------------------------------------------------------------------------

# join
lst = ['Hello', 'World', '!']
print(' '.join(lst))
print('\\'.join(lst))

print("#----------------------------------------------------#")
# split
stringOne = "Hello world !"
print(stringOne.split(' '))

print("#----------------------------------------------------#")
stringTwo = '''Hi
this is me Eng Osama
I hope that you are doing well'''
print(stringTwo.split('\n'))
print(stringTwo.splitlines())