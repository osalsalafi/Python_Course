# ----------------------------------------------------------------------------------------------
# -- 04. The modules sys, os and shutil to deal with the operating system and the file system --
# ----------------------------------------------------------------------------------------------
import sys
print(sys.platform) #win32

if sys.platform.startswith('win32') :
    print("Your are using Windows")
elif sys.platform.startswith('linux') :
    print("Your are using Linux")
elif sys.platform.startswith('darwin') :
    print("Your are using macOS")

# winreg >> sys.platform >> sys.path
print(sys.path)

# verison
print(sys.version) #3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)]
if sys.version.startswith('3.9.2'):
    print("Your python version is up to date")
else : 
    print('You have to update')

print("#-----------------------------------------#")
import os