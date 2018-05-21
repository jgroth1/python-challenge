# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The total amount of revenue gained over the entire period

# The average change in revenue between months over the entire period

# The greatest increase in revenue (date and amount) over the entire period

# The greatest decrease in revenue (date and amount) over the entire period

# Financial Analysis
# ----------------------------
# Total Months: 25
# Total Revenue: $1241412
# Average Revenue Change: $216825
# Greatest Increase in Revenue: Sep-16 ($815531)
# Greatest Decrease in Revenue: Aug-12 ($-652794)


import os
import csv
from statistics import mean

# define path for file to be analyzed
file_path = os.path.join('../Data_Files/PyBank/raw_data', 'budget_data_1.csv')
# open file within the with statement save file object to bankfile
with open(file_path, newline='') as bankfile:
    # read using csv.reader save to bankdata
    bankdata = csv.reader(bankfile, delimiter=',')
    #skip headerline
    next(bankdata)
    # initialize list to contain the revenue, month and date, and month only
    revenue = []
    month_date = []
    month = []
    # loop through the rows of the bank data
    for row in bankdata:
        # append values to revenue values to revenue list, month and date to month_date list
        revenue.append(row[1])
        month_date.append(row[0])
        # split month date by '-' to obtain only the month. append the month only to month list 
        temp = row[0].split('-')
        month.append(temp[0])

