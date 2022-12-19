# --------------------------------------------------------------------------------------------------------
# -- Python Course => Work with Google Sheets => 04. Scan and search for specific data in Google Sheets --
# --------------------------------------------------------------------------------------------------------

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re
scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('testsheet.json', scopes)
file = gspread.authorize(credentials)

sheet = file.open('example').sheet1

# FIND
cell = sheet.find('2500')
print('Found first matching cell at row %s and col %s' %(cell.row, cell.col)) # Found first matching cell at row 5 and col 2

# FIND ALL
cells = sheet.findall('2500')
print(cells) # [<Cell R5C2 '2500'>, <Cell R6C2 '2500'>]
print('Found second matching cell at row %s and col %s' %(cells[1].row, cells[1].col)) # Found second matching cell at row 6 and col 2

# FIND REGULAR EXPRESSION
employee = re.compile(r'osama|khalid')
cell = sheet.findall(employee)
print(cell) # [<Cell R2C1 'osama'>, <Cell R5C1 'khalid'>]

# BATCH CLEAR
sheet.batch_clear(['D1:D8'])

# SHEET CLEAR
sheet.clear()