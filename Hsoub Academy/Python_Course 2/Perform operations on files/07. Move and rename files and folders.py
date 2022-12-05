# -------------------------------------------------------------------------------------------
# -- Python Course => Perform operations on files => 07. Move and rename files and folders --
# -------------------------------------------------------------------------------------------

# The shutil module offers a number of high-level operations on files and collections 
# of files. In particular, functions are provided which support file copying and 
# removal. For operations on individual files, see also the os module.

# https://docs.python.org/3/library/shutil.html

import shutil
from pathlib import Path

# shutil.move(Path.home()/Path('Desktop','file','file_one_copied.txt'), Path.home()/ Path('Desktop','file','folder one backup'))
# shutil.move(Path.home()/Path('Desktop','file','file_one_copied.txt'), Path.home()/ Path('Desktop','file','folder one backup','file_one.txt'))

# if we move the file to non-existed folder it will change the file. to the default and move it
# so must be careful about the path

# if u tried to move a file with a name that exists in another file it will give u an error

# you can change the name of the file
# shutil.move(Path.home()/Path('Desktop','file','test.txt'), Path.home()/ Path('Desktop','file','file_two.txt'))
# or by using rename method from os library
import os
os.rename(Path.home()/ Path('Desktop','file','file_two.txt'),Path.home()/ Path('Desktop','file','file_two_os.txt'))
