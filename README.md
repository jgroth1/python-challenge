# python-challenge

## PyBank:

 Created a Python script that analyzes the records to calculate each of the following:

 The total number of months included in the dataset

 The total amount of revenue gained over the entire period

 The average change in revenue between months over the entire period

 The greatest increase in revenue (date and amount) over the entire period

 The greatest decrease in revenue (date and amount) over the entire period

 Output in the form of:
#
 Financial Analysis
# ----------------------------
 Total Months: 25

 Total Revenue: $1241412

 Average Revenue Change: $216825

 Greatest Increase in Revenue: Sep-16 ($815531)

 Greatest Decrease in Revenue: Aug-12 ($-652794)
#
### Created two different files for this project.

### main.py:
uses basic sequential programing methods.

### main_modular.py and bank_module.py:

uses simple functional programing methods and created a module (bank_module.py) to store the functions used in the main script main_modular.py and searches the directory and runs all files that contain .csv.

## PyBoss:

 Imports the employee data csv files, which currently holds employee records like the below:

 Emp ID,Name,DOB,SSN,State
 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
 15,Samantha Lara,1993-09-08,848-80-7526,Colorado
 411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania

 Then converted and exported the data to use the following format instead:

 Emp ID,First Name,Last Name,DOB,SSN,State

 214,Sarah,Simpson,12/04/1985,***-**-8166,FL

 15,Samantha,Lara,09/08/1993,***-**-7526,CO

 411,Stacy,Charles,12/20/1957,***-**-8526,PA

 In summary, the required conversions are as follows:

 The Name column should be split into separate First Name and Last Name columns.

 The DOB data should be re-written into MM/DD/YYYY format.

 The SSN data should be re-written such that the first five numbers are hidden from view.

 The State data should be re-written as simple two-letter abbreviations.


## PyPoll:
For this project the election results were imported and the following was calculated:

1. The total number of votes cast

2. A complete list of candidates who received votes

3. The percentage of votes each candidate won

4. The total number of votes each candidate won

5. The winner of the election based on popular vote.

 ### Out put is formated as follows:
#
 Election Results
# -------------------------
 Total Votes: 620100
# -------------------------
 Rogers: 36.0% (223236)

 Gomez: 54.0% (334854)

 Brentwood: 4.0% (24804)

 Higgins: 6.0% (37206)
# -------------------------
 Winner: Gomez
# -------------------------

#
## PyParagraph

 Import a text file filled with a paragraph of your choosing.

 Asseses the passage for each of the following:

     Approximate word count

     Approximate sentence count

     Approximate letter count (per word)

     Average sentence length (in words)

 ### Example output:

 Paragraph Analysis
# -----------------
 Approximate Word Count: 122

 Approximate Sentence Count: 5

 Average Letter Count: 4.56557377049

 Average Sentence Length: 24.4