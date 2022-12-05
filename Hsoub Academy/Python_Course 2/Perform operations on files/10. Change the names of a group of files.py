# ----------------------------------------------------------------------------------------------
# -- Python Course => Perform operations on files => 10. Change the names of a group of files --
# ----------------------------------------------------------------------------------------------
import os, shutil, re
from pathlib import Path
datepattern = '^(.*?)((0|1)?\\d)-((0|1|2|3)?\\d)-((19|20)\\d\\d)(.*?)$'

for filename in os.listdir(Path.home()/Path('Desktop','test')) :
    search = re.search(datepattern, filename)

    if search == None :
        continue

    beforePart = search.group(1)
    monthPart = search.group(2)
    dayPart = search.group(4)
    yearPart = search.group(6)
    afterPart = search.group(8)

    newfilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    print(f'Renameing "{filename}" to "{newfilename}"')

    oldName = Path.home() / Path('Desktop', 'test') / filename
    newName = Path.home() / Path('Desktop', 'test') / newfilename

    shutil.move(oldName,newName)