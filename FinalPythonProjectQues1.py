#QUES 1. What is the average median income of the data set and check the distribution of data using appropriate plots. Please explain the distribution of the plot.


import matplotlib.pyplot as plt  #libraries for graphical representation
import openpyxl  #library for working with Excel files
import pandas as pd  #library for data manipulation and analysis

excel_file = 'housing+(1).xlsx'  #name of the Excel file
workbook = openpyxl.load_workbook(excel_file)  #load the Excel file
sheet = workbook['housing (2) (1)']  #select the sheet from the Excel file

# Calculate average median income
median_income_data = [
    int(row[7]) for i, row in enumerate(sheet.iter_rows(values_only=True))
    if i > 0
]  #count number of rows and collect data
average_median_income = sum(median_income_data) / len(
    median_income_data)  # calculating avg median_income

# Print average median income
print("Average Median Income:", average_median_income)

# Plot histogram for Median Income
df_median_income = pd.DataFrame(
    median_income_data, columns=['Median Income']
)  #DataFrame is key data structures make it easy to perform data cleaning, manipulation, and analysis tasks.
plt.hist(df_median_income['Median Income'], bins=10)  #histogram plot
plt.title("Distribution of Median Income")  #title pf graph
plt.xlabel("Median Income")  #x-axis label
plt.ylabel("Frequency")  #y-axis label
plt.show()  #show graph
