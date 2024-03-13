
import openpyxl
import pandas as pd

excel_file = 'housing+(1).xlsx'
workbook = openpyxl.load_workbook(excel_file)
sheet = workbook['housing (2) (1)']

def calculate_median(data_set): # def is used to create user defined function
  sorted_data = sorted(data_set) # sorted is used to sort the data
  n = len(sorted_data)  # n is used to calculate the length of the data
  if n % 2 == 0:
      mid1 = sorted_data[n // 2]   # mid1 is used to calculate the median
      mid2 = sorted_data[(n // 2) - 1]  # mid2 is used to calculate the median
      median = (mid1 + mid2) / 2  # median is used to calculate the median
  else:
      median = sorted_data[n // 2]
  return median
my_data = [1,2,3,4,5,6,7,8,9]
result = calculate_median(my_data)
print(result)
