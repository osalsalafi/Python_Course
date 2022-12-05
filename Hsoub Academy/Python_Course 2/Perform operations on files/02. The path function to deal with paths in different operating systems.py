# -----------------------------------------------------------------------------------------------------------------------------
# -- Python Course => Perform operations on files => 02. The path function to deal with paths in different operating systems --
# -----------------------------------------------------------------------------------------------------------------------------

# since we having two diffrenet methods to deal with the paths in windows and in Mac
# so we must have a function that can work with both of them

# using the cammand line u can call the Path class from pathlib library
# >>> from pathlib import Path
# >>> Path('My Git-Hub','Python_Course','Hsoub Academy','Python_Course 2','Perform operations on files')
# WindowsPath('My Git-Hub/Python_Course/Hsoub Academy/Python_Course 2/Perform operations on files')
# >>> str(Path('My Git-Hub','Python_Course','Hsoub Academy','Python_Course 2','Perform operations on files'))
# 'My Git-Hub\\Python_Course\\Hsoub Academy\\Python_Course 2\\Perform operations on files'

# if we wrote the same in Mac we will get forward slash path

# >>> homeFolder = Path('C:/My Git-Hub/Python_Course/Hsoub Academy/Python_Course 2')
# >>> subFolder = Path('Perform operations on files')
# >>> homeFolder / subFolder
# WindowsPath('C:/My Git-Hub/Python_Course/Hsoub Academy/Python_Course 2/Perform operations on files')
# >>> str(homeFolder / subFolder)
# 'C:\\My Git-Hub\\Python_Course\\Hsoub Academy\\Python_Course 2\\Perform operations on files'