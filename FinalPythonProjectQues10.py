import openpyxl
import pandas as pd

excel_file = 'housing+(1).xlsx'
workbook = openpyxl.load_workbook(excel_file)
sheet = workbook['housing (2) (1)']
# Create a new column named total_bedroom_size
sheet['F1'] = 'total_bedroom_size'  # add a new column

for row in range(2, sheet.max_row + 1): # iterate through all rows
  total_bedroom_size = sheet['E' + str(row)].value  # get the value of the bedroom size column
  if total_bedroom_size is not None and total_bedroom_size <= 10: # check if the bedroom size is not null and less than or equal to 10
    sheet['F' + str(row)] = 'small'  # add a new column with the value 'small'
  elif total_bedroom_size is not None and total_bedroom_size >= 11 and total_bedroom_size < 1000: # check if the bedroom size is not null and greater than or equal to 11 and less than 1000
    sheet['F' + str(row)] = 'medium'  # add a new column with the value 'medium'
  else:
    sheet['F' + str(row)] = 'large'  # add a new column with the value 'large'
workbook.save('housing+(1)new1.xlsx')  # save the workbook
