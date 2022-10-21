from typing import List
def returnStringLetters(string1: str, string2: str) -> int:
    # write your code here ^_^
    if len(string1) > len(string2):
        return len(string1)
    else :
        return len(string2)


string1 = 'Ahmad'
string2 = 'Mohammad'
print(returnStringLetters(string1, string2))