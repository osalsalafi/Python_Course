# ----------------------------------
# -- Working with files in Python --
# ----------------------------------

f = open('text.txt',"w") # "W" >> to write
# if the file is not in the same directory copy the path
# C:\My Git-Hub\Python_Course\Hsoub Academy\Python basics\Dealing with errors
# f = open('C:\\My Git-Hub\\Python_Course\\Hsoub Academy\\Python basics\\Dealing with errors\\text.txt',"w")
f.write("Hello world!")
f.close()

f = open('text.txt',"r") # "r" >> to read
print(f.read())
f.close()

print("#" * 50)
#------------------------------------------------------------------------------#
f = open('text.txt',"w")
f.write("Hello world!\n")
f.write("You are the best")
f.close()

f = open('text.txt',"r")
print(f.read())
f.close()
print("#" * 50)
#------------------------- read specific range --------------------------------#
f = open('text.txt',"r")
print(f.read(10))
f.close()
#------------------------- read line by line ----------------------------------#
f = open('text.txt',"r")
print(f.readline())
f.close()
#----------------------- read line is iterable --------------------------------#
f = open('text.txt',"r")
for line in f :
    print(line, end="")
f.close()
print("\n")
#----------------- to avoid forgetting the close function ---------------------#
with open('text.txt','r') as f :
    print(f.read())
#----------------- use the appendex to avoid loosing data ---------------------#
f = open('text.txt',"a")
f.write("\nOsama is a good programmer")
f.close()
with open('text.txt','r') as f :
    print(f.read())
#----------------- you can open two files at the same time --------------------#
with open('text.txt',"a") as f , open('text2.txt','w') as f2 :
    f.write("\nThis is file one")
    f2.write("This is file two")

with open('text.txt',"r") as f , open('text2.txt','r') as f2 :
    print(f.read(), f2.read())
#--------------- to copy the content of one file to another -------------------#
with open('text.txt',"r") as f , open('text2.txt','w') as f2 :
    f_lines= f.read()
    f2.write(f_lines+"\nThis is a copy of text file")

with open("text2.txt","r") as f2 :
    print(f2.read())
