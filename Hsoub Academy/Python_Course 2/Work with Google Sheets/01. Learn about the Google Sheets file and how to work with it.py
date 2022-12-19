# ----------------------------------------------------------------------------------------------------------------
# -- Python Course => Work with Google Sheets => 01. Learn about the Google Sheets file and how to work with it --
# ----------------------------------------------------------------------------------------------------------------

# Firstly we have to connect our google account to the cloud of google from the console
# go to >> console.cloud.google.com
# create a new project
# go to >> API and service >> Library
# search for google sheets api and enable it
# search for google drive api and enable it
# go to >> API and service >> credintials
# go to >> create credentials >> service account 
# go to >> the sevice account >> keys >> create new key >> JSON
# take the file to the project folder and copy the client email and share it with the google sheet file

# ------------------------------------------------------------------------------------------------------

# from python side >>
# you will use gspead library to deal with google sheets
# 'gspread' is a python api for google sheets
# >> pip install gspread
# we have to install web authorization frame work
# >> pip install oauth2client
# the autho is a service to request and access to the accounts of the users in http pages

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# you have to add the scope 
# go to >> developers.google.com/sheets/api
# search for >> authorize requests
# https://developers.google.com/sheets/api/quickstart/python
# https://www.googleapis.com/auth/spreadsheets.readonly >> read only the user's sheets and their properties
# https://www.googleapis.com/auth/spreadsheets >> read/write the user's sheets and their properties
# https://www.googleapis.com/auth/drive.readonly >> read only the user's file metadata and file content
# https://www.googleapis.com/auth/drive.file >> pre-file access to files created or opened by the app
# https://www.googleapis.com/auth/drive >> Full, premissive scope access all of the user's files. Just when necessary

scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('testsheet.json', scopes)
file = gspread.authorize(credentials)
sheet = file.open('test2').sheet1

sheet.update_cell(2,3,'Osama Alsalafi')

