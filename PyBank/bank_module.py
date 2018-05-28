""" Module for bank analysis project.  """

import os
import csv
import fnmatch
from statistics import mean

def extract_data_csv(file_path, newline=''):
    """
    Opens file and extracts the revenue, month_date, and the month only from
    the .csv file.
    inputs:
    file_path = path to the file that is to be analyzed
    newline = newline method can be None, '', '\n', '\r', and '\r\n'. defalt is 
    ''.
    outputs:
    revenue = returns a list of all the revenue changes for the period 
    anlayized.
    month_date = returns list of all months and dates in Month-date format.
    month = returns only a list of months only
    """
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
    return revenue, month_date, month

def Number_of_Unique_Items(duplicate_list):
    """
    determine the number of unique items in the list by converting the list to a set that can only contain unique values then taking the length of the set using len.
    input:
    duplicate_list = list from the original csv file that contains
    duplicates of months
    output:
    num_unique_items = value coresponding to the number of unique items in the input list
    """
    unique_set = set(duplicate_list)
    num_unique_items = len(unique_set)
    return num_unique_items

def Extract_Files(file_path, pattern='None'):
    """
    extracts the file names in the directory given in file path and saves them
    to a list.  The function accepts pattern inputs that allow for file searches for specific file patterns using fnmatch.
    inputs:
    file_path = directory to list files from
    pattern = pattern of file search defalt to 'None' 
    output:
    list_of_files = list of files that match the pattern given if 'None' all files in directory are listed.
    """
    if pattern == 'None':
        list_of_files = os.listdir(file_path)
    else:
        files = os.listdir(file_path)
        list_of_files = []
        for file in files:
            if fnmatch.fnmatch(file, pattern):
                list_of_files.append(file)
    return list_of_files

if __name__ == "__main__":
    print('this is a module. please import bank_module or run main_modular.py')