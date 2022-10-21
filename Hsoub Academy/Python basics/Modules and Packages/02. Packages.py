# --------------
# -- Packages --
# --------------
print("#-----------------------------------#")
# import my_packages.pack1 as m1 , my_packages.pack2 as m2
# m1.mod1()
# m2.mod2()
print("#-----------------------------------#")
# from my_packages.pack1 import mod1
# from my_packages.pack2 import mod2
# mod1()
# mod2()
print("#-----------------------------------#")
#__init__.py
# import my_packages
# from my_packages import pack1,pack2
# The name of this package is my_packages
print("#-----------------------------------#")
# import my_packages
# my_packages.pack1.mod1()
# my_packages.pack2.mod2()
print("#-----------------------------------#")
# import my_packages.subpackage.subpack1 as subpack
# import my_packages
# subpack.subpack()
# print(dir())
print("#-----------------------------------#")
from my_packages import *
print(dir())