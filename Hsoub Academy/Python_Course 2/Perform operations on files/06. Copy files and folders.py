# --------------------------------------------------------------------------------
# -- Python Course => Perform operations on files => 06. Copy files and folders --
# --------------------------------------------------------------------------------

# The shutil module offers a number of high-level operations on files and collections 
# of files. In particular, functions are provided which support file copying and 
# removal. For operations on individual files, see also the os module.

# https://docs.python.org/3/library/shutil.html

import shutil
from pathlib import Path

print(Path.home()) # C:\Users\Dell

# ---------------------------- Copy file
# shutil.copy(Path.home()/Path('file_one.txt'),Path.home()/Path('Desktop','file'))
# shutil.copy(Path.home()/Path('file_one.txt'),Path.home()/Path('Desktop','file','file_one_copied.txt'))

# ---------------------------- Copy folder
shutil.copytree(Path.home()/Path('folder one'), Path.home()/Path('Desktop','file','folder one backup'))
