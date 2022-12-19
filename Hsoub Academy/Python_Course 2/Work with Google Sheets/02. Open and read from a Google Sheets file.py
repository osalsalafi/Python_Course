# ---------------------------------------------------------------------------------------------
# -- Python Course => Work with Google Sheets => 02. Open and read from a Google Sheets file --
# ---------------------------------------------------------------------------------------------


import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('testsheet.json', scopes)

file = gspread.authorize(credentials)
# sheet = file.open('test2').sheet1
# we can open the file by using the url of the file
sheet = file.open_by_url('https://docs.google.com/spreadsheets/d/1cXriMKQ421ZnDPTvme9-2oytZLQJktyVyC-cp03K1GI/edit?usp=sharing')

worksheet1 = sheet.get_worksheet(0)
print(worksheet1) # <Worksheet 'Sheet1' id:0>
worksheet1 = sheet.worksheet('Sheet1')
print(worksheet1) # <Worksheet 'Sheet1' id:0>
worksheets = sheet.worksheets()
print(worksheets) # [<Worksheet 'Sheet1' id:0>]

# READ FROM SHEETS
val = worksheet1.acell('A1').value
print(val) # osama
val = worksheet1.cell(1,1).value
print(val) # osama

salaries = worksheet1.col_values(2)
print(salaries) # ['1000', '1500', '2000', '2500', '3000', '3500']

wholeworksheet = worksheet1.get_all_values()
print(wholeworksheet) # [['osama', '1000', '10/1/2010'], ['ahmed', '1500', '15-2-2021'], ['ali', '2000', '16-8-2009'], ['khalid', '2500', '17-2-2019'], ['salem', '3000', '17-2-2019'], ['mohammed', '3500', '18-12-2022']]

# if we want to print the value in a dictionary where the keys are the value of the first row
wholeworksheet = worksheet1.get_all_records()
print(wholeworksheet) # [{'name': 'osama', 'salary': 1000, 'date of join': '10/1/2010'}, {'name': 'ahmed', 'salary': 1500, 'date of join': '15-2-2021'}, {'name': 'ali', 'salary': 2000, 'date of join': '16-8-2009'}, {'name': 'khalid', 'salary': 2500, 'date of join': '17-2-2019'}, {'name': 'salem', 'salary': 3000, 'date of join': '17-2-2019'}, {'name': 'mohammed', 'salary': 3500, 'date of join': '18-12-2022'}]
