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
file = 'budget_data_2.csv'
file_path = os.path.join('../Data_Files/PyBank/raw_data', file)
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
        revenue.append(float(row[1]))
        month_date.append(row[0])
        # split month date by '-' to obtain only the month. append the month only to month list 
        temp = row[0].split('-')
        month.append(temp[0])

# determine the number of months by converting the list to a set that can only contain unique values then taking the length of the set using len
month_set = set(month)
num_months = len(month_set)

# compute total revenue using the sum()
total_revenue = round(sum(revenue), 2)

# compute average revenue change by using mean() from the statistics package
avg_revenue = round(mean(revenue), 2)


# find the greatest increase in revenue using max() and find the index using the .index() method
max_value = max(revenue)
max_index = revenue.index(max_value)

# find the greatest decrease in revenue using min() and find the index using the .index() method
min_value = min(revenue)
min_index = revenue.index(min_value)

# find the month and date that coresponds to the greatest increase and decrease in revenue using the month_date list and index in max_index and min_index
max_date = month_date[max_index]
min_date = month_date[min_index]

# print output
print('','Financial Analysis', '-----------------------', 'Total Months: ' + str(num_months), 'Total Revenue: $' + str(total_revenue), 'Average Revenue Change: $' + str(avg_revenue),'Greatest Increase in Revenue: ' + max_date + '($' + ' ' + str(max_value) + ')', 'Greatest Decrease in Revenue: ' + min_date + '($' + ' ' + str(min_value) + ')', '',sep='\n',)