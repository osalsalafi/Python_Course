# ------------------------------------------------------------------------------------------------------
# -- Python Course => Dealing with Excel spreadsheets => 04. Mathematical functions in Excel formulas --
# ------------------------------------------------------------------------------------------------------
import openpyxl
from pathlib import Path

excelfile = openpyxl.load_workbook('C:\\My Git-Hub\\Python_Course\\Hsoub Academy\\Python_Course 2\\Dealing with Excel spreadsheets\\test1.xlsx')

Sheet = excelfile['Sheet1']

# Sheet['B7'] = '=SUM(B1:B6)'
# Sheet['B7'] = '=average(B1:B6)'
Sheet['B7'] = '=COUNTIF(B1:B6, ">750")'

excelfile.save('C:\\My Git-Hub\\Python_Course\\Hsoub Academy\\Python_Course 2\\Dealing with Excel spreadsheets\\test1.xlsx')

# for more functions in Excel
# https://academy.hsoub.com/apps/productivity/office/microsoft-excel/%D8%A3%D9%83%D8%AB%D8%B1-%D8%A7%D9%84%D8%AF%D9%88%D8%A7%D9%84-%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6%D9%8A%D8%A9-%D8%B4%D9%8A%D9%88%D8%B9%D8%A7-%D9%81%D9%8A-%D9%85%D8%A7%D9%8A%D9%83%D8%B1%D9%88%D8%B3%D9%88%D9%81%D8%AA-%D8%A5%D9%83%D8%B3%D9%84-r449/