# -------------------------------------------------------------------------------------------
# -- Python Course => Perform operations on files => 09. Dealing with compressed zip files --
# -------------------------------------------------------------------------------------------
import zipfile
from pathlib import Path
import os

# to read a zip file
compressZip = zipfile.ZipFile(Path.home()/Path('Desktop','file.zip'))
print(compressZip.namelist())
# ['file/', 'file/file_one.txt', 'file/file_two_os.txt', 'file/folder one backup/', 'file/folder one backup/file_one_copied.txt']

# to get info about a specific file in the zip file
fileinfo = compressZip.getinfo('file/file_one.txt')
print(fileinfo.file_size) # 0
print(fileinfo.compress_size) # 0

# extract
# I have to change the working directory to extract the items to
os.chdir(Path.home()/Path('Desktop'))
compressZip.extractall()
# or extract specific file
compressZip.extract('file/file_one.txt',Path.home()/Path('Desktop','extract_file'))

# compress file
newZip = zipfile.ZipFile('New_Zip.zip', 'w')
newZip.write('file/file_one.txt')

# compress folder 
newZip = zipfile.ZipFile('New_Zip2.zip', 'w')
newZip.write(Path.home()/Path('Desktop','extract_file'))
# we will face an issue that the folder here will be comporessed without the files
import shutil
shutil.make_archive('New_zip3','zip', Path.home()/Path('Desktop','extract_file'))


# ---------------------------------------------------------------------------------------
# zipfile.Zipfile()
# file.namelist()
# = file.getinfo()
# = file2.file_size
# = file2.compress_size
# file.extractall()
# file.extract
# new_file = zipfile.Zipfile(name,mode)
# new_file.write()
# shutil.make_archive(name,zip,folder path)