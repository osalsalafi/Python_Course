# ------------------ w
# my_file = open('file_three.txt','w') # if there is no file with this name it will be created
# my_file.write('10. Hi This is me Eng. Osama' + '11. Hi This is me Eng. Osama' + '12. Hi This is me Eng. Osama')
# # 'w' will write over the previous text and remove it

# ------------------ writelines
# # to write a list in a file use writelines
# my_list = ['\n13. Hi This is me Eng. Osama\n','14. Hi This is me Eng. Osama\n','15. Hi This is me Eng. Osama\n']
# my_file.writelines(my_list)

# ------------------ a
my_file = open('file_three.txt','a') # if there is no file with this name it will be created
my_file.write('16. Hi This is me Eng. Osama\n' + '17. Hi This is me Eng. Osama\n' + '18. Hi This is me Eng. Osama')
# 'a' will append over the previous text

my_file.close()
