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
import bank_module as bm
# define path to be searched
path = '../Data_Files/PyBank/raw_data'

# list files in directory
files = bm.Extract_Files(path, pattern='*.csv')

# loop through files
for file in files:
# define path for file to be analyzed
    file_name = file

    
    file = file_name
    file_path = os.path.join(path, file)
    # open file extract the revenue, month_date and month data from the csv file
    revenue, month_date, month = bm.extract_data_csv(file_path, newline='')
    # determine the number of months by converting the list to a set that can only contain unique values then taking the length of the set using len
    num_months = bm.Number_of_Unique_Items(month)

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
    print('','Financial Analysis', '-----------------------', 'Total Months: ' + str(num_months), 'Total Revenue: $' + str(total_revenue), 'Average Revenue Change: $' + str(avg_revenue),'Greatest Increase in Revenue: ' + max_date + ' ' + '($' + str(max_value) + ')', 'Greatest Decrease in Revenue: ' + min_date + ' ' + '($' + str(min_value) + ')', '',sep='\n')

    out = 'Output_'
    form = '.txt'
    file = out + file_name[0:-4] + form 
    output_file = os.path.join(file)
    with open(output_file, 'w') as outfile:
        outfile.writelines('Financial Analysis')
        outfile.writelines('\n' + '-----------------------')
        outfile.writelines('\n' + 'Total Months: ' + str(num_months))
        outfile.writelines('\n' + 'Total Revenue: $' + str(total_revenue))
        outfile.writelines('\n' + 'Average Revenue Change: $' + str(avg_revenue))
        outfile.writelines('\n' + 'Greatest Increase in Revenue: ' + max_date + ' ' + '($' + str(max_value) + ')')
        outfile.writelines('\n' + 'Greatest Decrease in Revenue: ' + min_date + ' ' + '($' + str(min_value) + ')')
