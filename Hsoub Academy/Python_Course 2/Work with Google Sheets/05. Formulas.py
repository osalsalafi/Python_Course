# --------------------------------------------------------------
# -- Python Course => Work with Google Sheets => 05. Formulas --
# --------------------------------------------------------------


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re
scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('testsheet.json', scopes)
file = gspread.authorize(credentials)

new_file = file.open('example')

sheet = new_file.get_worksheet(0)

sheet.update_cell(8,2,'=SUM(B2:B7)')
sheet.update_cell(9,2,'=MAX(B2:B7)')
sheet.update_cell(10,2,'=MIN(B2:B7)')
sheet.update_cell(11,2,'=AVERAGE(B2:B7)')

cell = sheet.acell('B10', value_render_option='FORMULA').value
print(cell) # =MIN(B2:B7)


