import openpyxl
import pandas as pd

excel_file = 'housing+(1).xlsx'
workbook = openpyxl.load_workbook(excel_file)
sheet = workbook['housing (2) (1)']

df = pd.read_excel(excel_file)  #read the Excel file, create a Pandas DataFrame (df) containing the data from the Excel file. You can then use this DataFrame to manipulate, analyze, and work with the data within your Python script


near_ocean_data = df[df['ocean_proximity'] == 'Near ocean']  ## selecting rows with ocean_proximity = 'Near ocean'

# Export the dataset to Excel format
export_path = 'near_ocean_data.xlsx'  # Specify the path where you want to save the Excel file

near_ocean_data.to_excel(export_path, index=False)  

# Calculate the mean and median of the median income
mean_income = near_ocean_data['median_income'].mean()  # Calculate the mean of the median income
median_income = near_ocean_data['median_income'].median()  # Calculate the median of the median income

print("Mean Median Income:", mean_income)  # Print the mean income
print("Median Median Income:", median_income)  # Print the median income
