# ---------------------------
# -- pip . package manager --
# ---------------------------
# pip = package installer provider

# All the packages are stores in this path
# C:\Users\Dell>python -q
# >>> import site
# >>> site.getsitepackages()
# ['C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']

# C:\My Git-Hub\Python_Course\Hsoub Academy\Python basics\Modules and Packages>mkdir my_python_project

# C:\My Git-Hub\Python_Course\Hsoub Academy\Python basics\Modules and Packages>cd my_python_project

# C:\My Git-Hub\Python_Course\Hsoub Academy\Python basics\Modules and Packages\my_python_project>python -m venv venv

# ----------- In Linux --------------
# C:\My Git-Hub\Python_Course\Hsoub Academy\Python basics\Modules and Packages\my_python_project>python3-venv
# ----------- if using VPN
# C:\My Git-Hub\Python_Course\Hsoub Academy\Python basics\Modules and Packages\my_python_project>sudo apt install python3-venv

print("#---------------------------------------------------------------------------#")
# ----------- To activate the environment in Linux & Mac
# C:\My Git-Hub\Python_Course\Hsoub Academy\Python basics\Modules and Packages\my_python_project>source venv/bin/activate
# ----------- To activate the environment in Windows
# C:\My Git-Hub\Python_Course\Hsoub Academy\Python basics\Modules and Packages\my_python_project>venv\Scripts\activate
# (venv) C:\My Git-Hub\Python_Course\Hsoub Academy\Python basics\Modules and Packages\my_python_project> >> that means we can install the packages in this file without effecting the other versions
# ----------- To quit from the evironment ======= deactivate
# ----------- To get the available library ====== pip or pip3
# ----------- To get the pip version ====== pip --version
# ----------- you can get the packages from this link https://pypi.org/
# ----------- for example you can install flask framework for web development >> pip install Flask
# ----------- To know the installed one >> pip list
# ----------- To get info about a package >> pip show click
# ----------- You have to create the required packages for the project to be implemented directly >> you can add them in Requirement.txt
# ----------- You can save them by using this comman ====== pip freeze > requirements.txt
# ----------- You can upgrade the packages that has been used in the project  ====== pip install --upgrade -r requirements.txt
# ----------- You can install the packages of the project in another directory of PC ===== pip install -r requirements.txt
# ----------- You can uninstall the packages ============ pip uninstall flask
# ----------- You can remove all packages ========== pip uninstall -r requirements.txt
print("#---------------------------------------------------------------------------#")
# ----------- In package.Json >> 1. Dev.dependencies for developments, 2. Dependencies for basics
print("#---------------------------------------------------------------------------#")
# ----------- We have another package managers such as "Conda", "Pipenv", "Poetry"