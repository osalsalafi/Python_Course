# -------------------------------------------------------------------------------------------------------------------------
# -- Python Course => Dealing with Excel spreadsheets => 06. Create a multiplication table and write it to an Excel file --
# -------------------------------------------------------------------------------------------------------------------------
# ----------------------------------- Project about dealing with excel file using python ----------------------------------
import openpyxl, sys
from pathlib import Path
from openpyxl.styles import Font

if len(sys.argv) == 2 :
    try :
        number = int(sys.argv[1]) # 5
    except Exception as e :
        print(e)

    excelfile = openpyxl.Workbook()
    Sheet = excelfile.active

    for x in range(number + 1):
        for y in range (number + 1) :
            isheader = False
            if x == 0 and y == 0 :
                isheader = True
                n = ''
            elif x == 0 :
                isheader = True
                n = y
            elif y == 0 :
                isheader = True
                n = x
            else :
                n = x * y
            
            cell = Sheet.cell(row=y+1, column=x+1)
            cell.value = n

            if isheader :
                cell.font = Font(bold=True)
            
            excelfile.save(f"C:\\My Git-Hub\\Python_Course\\Hsoub Academy\\Python_Course 2\\Dealing with Excel spreadsheets\\Project for {number} multiplication table.xlsx")






else :
    print('Please enter only two arguments')


