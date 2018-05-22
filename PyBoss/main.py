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

# set up dictionary of state names to abriviations taken from https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# set file path
file = 'employee_data1.csv'
file_path = os.path.join('../Data_Files/PyBoss/raw_data', file)

# Open file with in the with operator and read using csv.reader
with open(file_path, newline='') as data_file:
    employee_data = csv.reader(data_file, delimiter=',')
    # skip header line
    next(employee_data)
    # list for id, first name, dob, ssn, and state 
    ID = []
    FirstName = []
    LastName = []
    DOB = []
    SSN = []
    State = []

    # Loop through the rows of empoyee_data
    for row in employee_data:
        ID.append(row[0])
        temp = row[1].split(' ')
        FirstName.append(temp[0])
        LastName.append(temp[1])
        temp = row[2].split('-')
        temp1 = temp[1] + '/' + temp[2] + '/' + temp[0]
        DOB.append(temp1)
        temp = row[3].split('-')
        temp1 = '***-**-' + temp[2]
        SSN.append(temp1)
        temp = us_state_abbrev[row[4]]
        State.append(temp)

header = ['ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
new_employee_list = []
for i in range(len(ID)):
    new_employee_dict = {}
    new_employee_dict[header[0]] = ID[i]
    new_employee_dict[header[1]] = FirstName[i]
    new_employee_dict[header[2]] = LastName[i]
    new_employee_dict[header[3]] = DOB[i]
    new_employee_dict[header[4]] = SSN[i]
    new_employee_dict[header[5]] = State[i]
    new_employee_list.append(new_employee_dict)

with open('new_employee_data.csv', 'w') as datafile:
    writer = csv.DictWriter(datafile, fieldnames=header)

    writer.writeheader()
    writer.writerows(new_employee_list)