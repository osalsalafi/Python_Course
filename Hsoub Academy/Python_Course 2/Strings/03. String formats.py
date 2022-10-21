# ----------------------------------------------------
# -- Python Course => Strings => 03. String formats --
# ----------------------------------------------------
name = "Osama"
age = 26
CGPA = 3.66

# print("My name is " + name + ", and my age is "+ age)
print("My name is " + name + ", and my age is "+ str(age))

#-------------- % method ------------#
print("My name is %s, and my age is %d, and my CGPA is %.3f" %(name,age,CGPA))

#------------ str.format ------------#
print("My name is {}, and my age is {}, and my CGPA is {}".format(name,age,CGPA))
print("My name is {:s}, and my age is {:d}, and my CGPA is {:.2f}".format(name,age,CGPA))
# print("My name is {}, and my age is {}, and my CGPA is {}".format(age,CGPA,name))
print("My name is {2}, and my age is {0}, and my CGPA is {1}".format(age,CGPA,name))
print("My name is {name_key}, and my age is {age_key}, and my CGPA is {CGPA_key}".format(name_key=name,age_key=age,CGPA_key=CGPA))

#------------ f" string ------------#
print(f"My name is {name}, and my age is {age}, and my CGPA is {CGPA}")
