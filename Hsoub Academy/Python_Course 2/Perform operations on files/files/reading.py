#-------------------------------------- open () -------------------------------------------------------------
# open function takes two values :
# open ('file_name','operation_to_that_file')
# operations : 'a' >> append to the file
#              'r' >> read from the file ** it is the default choice
#              'w' >> write to the file
#              'x' >> create a file 

# myfile = open(r"C:\My Git-Hub\Python_Course\Hsoub Academy\Python_Course 2\Perform operations on files\files\file_one.txt",'r')
# myfile = open("file_one.txt",'r')
# or by the relative path   


# if I do not know the current path directory use the os methods
import os

#-------------------------------------- getcwd() -------------------------------------------------------------
print(os.getcwd())
# C:\My Git-Hub\Python_Course\Hsoub Academy\Python_Course 2\Perform operations on files\files

#-------------------------------------- chdir () -------------------------------------------------------------
# you can change the working directory by using the method
# os.chdir(r'new_directory')

#-------------------------------------- home () -------------------------------------------------------------
from pathlib import Path
print(Path.home()) # C:\Users\Dell

my_file2 = open('file_two.txt','r')

print(my_file2) # <_io.TextIOWrapper name='file_two.txt' mode='r' encoding='cp1252'>
# print(my_file2.read()) # file two content
# print(my_file2.read(9)) # print only nine indexes
# print(my_file2.readline()) # print only one line with \n
# print(my_file2.readlines()) # print lines in list # ['This is file two A\n', 'This is file two B\n', 'This is file two C']
lines = my_file2.readlines()
print(lines[1]) # This is file two B

# then we must close the file
my_file2.close()
