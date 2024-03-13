import matplotlib.pyplot as plt
import openpyxl


excel_file = 'housing+(1).xlsx'
workbook = openpyxl.load_workbook(excel_file)
sheet = workbook['housing (2) (1)']

latitude = [float(cell.value) for cell in sheet['B'][1:]]  # extracting B column data to latitude variable
longitude = [float(cell.value) for cell in sheet['A'][1:]]  # extracting A column data to longitude variable

plt.scatter(longitude, latitude)  # plotting scatter plot
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Latitude vs Longitude')
plt.show()
