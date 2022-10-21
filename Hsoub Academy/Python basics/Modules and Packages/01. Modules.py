# -------------
# -- Modules --
# -------------
# Modular Programming will deal with the Modules seperately
# qoutes.py is a module
print("#-------------------------------#")
# import quotes
# print(quotes.get_quotes())
print("#-------------------------------#")
# from quotes import get_quotes
# print(get_quotes())
print("#-------------------------------#")
# from quotes import *
# print(get_quotes())
print("#-------------------------------#")
# from quotes import get_quotes as quotes
# print(quotes())
print("#-------------------------------#")
# import quotes as q
# print(q.get_quotes())
print("#-------------------------------#")
# def get_quotes_module():
#     from quotes import get_quotes as quotes
#     print(quotes())
# get_quotes_module()
print("#-------------------------------#")
# def get_quotes_module():
#     from quotes import get_quotes
#     print(get_quotes())
# get_quotes_module()
print("#-------------------------------#")
# we can use - try\except :
# try :
#     from quotes import get_quote
# except :
#     print("Module not found")
print("#-------------------------------#")
import quotes
print(quotes.get_quotes())


# to be able to know the path of import --- import sys ---
# import sys
# print(sys.path)