from typing import List
def numToEng(n: int) -> str:
    # write your code here ^_^
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
    
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = "hundred"
    n1 = [int(index) for index in str(n)]
    if n < 20 :
        return f"{units[n]}"
    elif n < 100 :
        if n1[1] == 0 :
            return f"{tens[n1[0]]}"
        else :
            return f"{tens[n1[0]]} {units[n1[1]]}"
    elif n < 1000 :
        if int(str(n)[1:3]) < 20 :
            if n1[1] == 0 and n1[2] != 0:
                return f"{units[n1[0]]} {scales} {units[n1[2]]}"
            elif n1[1] == 0 and n1[2] == 0 :
                return f"{units[n1[0]]} {scales}"
            else :
                return f"{units[n1[0]]} {scales} {units[int(str(n)[1:3])]}"
        else :
            if n1[2] == 0 :
                return f"{units[n1[0]]} {scales} {tens[n1[1]]}"
            else :
                return f"{units[n1[0]]} {scales} {tens[n1[1]]} {units[n1[2]]}"
    else :
        return "The value is higher than 999"
    # if len(n1) == 1 :
    #     engnum = f"{units[n1[0]]}"
    #     return engnum
    # elif len(n1) == 2 and n < 20 :
    #     engnum = f"{units[n1[0]]}"
    #     return engnum