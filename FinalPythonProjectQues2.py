import matplotlib.pyplot as plt  #Library for graphical representation
import openpyxl  #library for working with Excel files
import pandas as pd     #library for data manipulation and analysis

excel_file = 'housing+(1).xlsx'  #name of the Excel file
workbook = openpyxl.load_workbook(excel_file)  #load the Excel file
sheet = workbook['housing (2) (1)']   #select the sheet from the Excel file

# Plot histogram for Housing Median Age
housing_age_data = [int(row[2]) for i, row in enumerate(sheet.iter_rows(values_only=True)) if i >0]   #get the median age of housing
df_housing_age = pd.DataFrame(housing_age_data, columns=['Housing Median Age'])  #create a dataframe with the median age

print(df_housing_age) #print the dataframe
plt.hist(df_housing_age['Housing Median Age'], bins=10)  #plot the histogram
plt.title("Distribution of Housing Median Age")
plt.xlabel("Housing Median Age")
plt.ylabel("Frequency")
plt.show()
