import os

#getcwd
#getchdir
# print(os.getcwd()) # C:\My Git-Hub\Python_Course\Hsoub Academy\Python basics\Python Standard Library\os folder
# os.chdir("folder1")
# print(os.getcwd()) # C:\My Git-Hub\Python_Course\Hsoub Academy\Python basics\Python Standard Library\os folder\folder1
# os.chdir("../folder2") #../ >> father folder
# print(os.getcwd()) # C:\My Git-Hub\Python_Course\Hsoub Academy\Python basics\Python Standard Library\os folder\folder2
# os.chdir("..")
# print(os.getcwd()) # C:\My Git-Hub\Python_Course\Hsoub Academy\Python basics\Python Standard Library\os folder

#listdir
print(os.listdir()) # ['folder1', 'folder2']

# scandir
print(os.scandir()) # <nt.ScandirIterator object at 0x00000235BA39AEC0>
content = os.scandir()
for index in content :
    print(index.name)
    # folder1
    # folder2

# is_file
for index in content :
    
    if index.is_file():
        print(index.name)
    # folder1
    # folder2


# mkdir
# os.mkdir('folder3')

#FileExistsError

#makedirs
# os.makedirs('folder3/folder4')

#rename
# os.rename('folder3/folder4','folder3/folder3.1')

#rmdir >> only empty
# os.rmdir('folder2')

print("#-----------------------------------#")
import shutil
# shutil.rmtree("file.name") # for folder with files

# shutil.copy('folder1/file1.txt', 'folder3/file.txt')

# if you want to copy the date of creation as well 
# shutil.copy2()

# you can move the file or change its name
# shutil.move()
# shutil.move('folder3/file.txt','folder3/file1.txt')


# for more info : https://wiki.hsoub.com/Python/os