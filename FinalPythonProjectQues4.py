import openpyxl
import pandas as pd
excel_file = 'housing+(1).xlsx'
workbook = openpyxl.load_workbook(excel_file)
sheet = workbook['housing (2) (1)']

# Create a data set in a new excel by deleting the corresponding examples for which total_bedrooms are not available
# Delete the row if total_bedrooms is not available

data = pd.read_excel(excel_file, sheet_name="housing (2) (1)")
data = data.dropna(subset=['total_bedrooms'])  # Delete the row if total_bedrooms is not available
data.to_excel("new_housing.xlsx", index=False)  # Save the new data set in a new excell
