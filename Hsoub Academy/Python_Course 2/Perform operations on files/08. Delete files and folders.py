# ----------------------------------------------------------------------------------
# -- Python Course => Perform operations on files => 08. Delete files and folders --
# ----------------------------------------------------------------------------------

import os
from pathlib import Path

# to remove a file 
# --------------------------------- os.unlink() -------------------------------------------

# to remove a folder 
# ---- if the folder is empty 
# --------------------------------- os.rmdir() --------------------------------------------
# os.rmdir(Path.home()/Path('Desktop','file','folder three'))
# ---- if the folder has files 
# --------------------------------- shutil.rmtree() ---------------------------------------
import shutil
# shutil.rmtree(Path.home()/Path('Desktop','file','folder three'))


# --- The previous methods will remove all the items permenantly 
# to have a save delete
# https://pypi.org/project/Send2Trash/
# pip install Send2Trash
# --------------------------------- send2trash.send2trash() -------------------------------
import send2trash
send2trash.send2trash(Path.home()/Path('Desktop','file','file four.txt'))
