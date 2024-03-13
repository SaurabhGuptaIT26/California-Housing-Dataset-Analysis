import matplotlib.pyplot as plt
import openpyxl
import pandas as pd

excel_file = 'housing+(1).xlsx'
workbook = openpyxl.load_workbook(excel_file)
sheet = workbook['housing (2) (1)']

# Read the data into a DataFrame
df = pd.DataFrame(sheet.values)  # sheet.values returns a 2D array
df.columns = df.iloc[0]  # rename the first row to column names
df = df.iloc[1:].astype({'median_income': float})  # convert to float
df['median_house_values'] = df['median_house_value'].astype(float) 

# Create a scatter plot
plt.scatter(df['median_income'], df['median_house_values'])  # x-axis is median_income, y-axis is median_house_values
plt.xlabel('Median Income')
plt.ylabel('Median House Values')
plt.title('Relationship between Median Income and Median House Values')

# Show the plot
plt.show()
