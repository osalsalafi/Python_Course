# --------------------------------------------------------------------------------------------
# -- Python Course => Work with Google Sheets => 03. Create and write data to Google Sheets --
# --------------------------------------------------------------------------------------------

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('testsheet.json', scopes)

file = gspread.authorize(credentials)

# CREATE A NEW FILE
# new_file = file.create('CreateAndWrite')
# if we go to our accont in google we will not find the file because the file has been created in the console email
# so we have to share the file with our email
# new_file.share('os.alsalafi@gmail.com', perm_type='user',role='writer')
# check the parameters of gspread liberary
# https://docs.gspread.org/en/v5.7.0/
# make it as owner to have it in ur files
# new_file.share('os.alsalafi@gmail.com', perm_type='user',role='writer')

# OPEN FILE
new_file = file.open('CreateAndWrite')

# CREATE A NEW SHEET
# sheet = new_file.add_worksheet(title='Sheet2', rows=100, cols=20)

# WRITE TO SHEET
worksheet = new_file.worksheet('Sheet2')
# worksheet.update_acell('A1', "Hello world!")
worksheet.update('A2', 'This is me Eng. Osama')

# if I have value of more than one cell I have to write the range
worksheet.update('A1:C2',[['Osama',6500,'9/5/2022'],['Ammar',6000,'11/12/2022']])