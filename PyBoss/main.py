# Import the employee_data1.csv and employee_data2.csv files, which currently holds employee records like the below:

# Emp ID,Name,DOB,SSN,State
# 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
# 15,Samantha Lara,1993-09-08,848-80-7526,Colorado
# 411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania

# Then convert and export the data to use the following format instead:

# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,12/04/1985,***-**-8166,FL
# 15,Samantha,Lara,09/08/1993,***-**-7526,CO
# 411,Stacy,Charles,12/20/1957,***-**-8526,PA

# In summary, the required conversions are as follows:

# The Name column should be split into separate First Name and Last Name columns.

# The DOB data should be re-written into MM/DD/YYYY format.

# The SSN data should be re-written such that the first five numbers are hidden from view.

# The State data should be re-written as simple two-letter abbreviations.

import os
import csv

# set file path
file = 'employee_data1.csv'
file_path = os.path.join('../Data_Files/PyBoss/raw_data', file)

with open(file_path, newline='') as data_file:
    employee_data = csv.reader(data_file, delimiter=',')

    new_employee_list = []
    for row in employee_data:
        