# --------------------------------------------------------------------
# -- Python Course => Dealing with Excel spreadsheets => 05. Charts --
# --------------------------------------------------------------------
import openpyxl
from pathlib import Path

excelfile = openpyxl.load_workbook('C:\\My Git-Hub\\Python_Course\\Hsoub Academy\\Python_Course 2\\Dealing with Excel spreadsheets\\test1.xlsx')

Sheet = excelfile['Sheet1']

# charts
names = openpyxl.chart.Reference(Sheet, min_col=1, max_col=1, min_row=1, max_row=6)
salaries = openpyxl.chart.Reference(Sheet, min_col=2, max_col=2, min_row=1, max_row=6)

# search for openpyxl charts
# https://openpyxl.readthedocs.io/en/stable/charts/introduction.html

chart = openpyxl.chart.BarChart() # >> LineChart()

chart.title = 'Company Chart'
chart.add_data (data= salaries)
chart.set_categories(names)
Sheet.add_chart(chart, 'E8')

excelfile.save('C:\\My Git-Hub\\Python_Course\\Hsoub Academy\\Python_Course 2\\Dealing with Excel spreadsheets\\test1.xlsx')