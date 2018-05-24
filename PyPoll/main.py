# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# Election Results
# -------------------------
# Total Votes: 620100
# -------------------------
# Rogers: 36.0% (223236)
# Gomez: 54.0% (334854)
# Brentwood: 4.0% (24804)
# Higgins: 6.0% (37206)
# -------------------------
# Winner: Gomez
# -------------------------

import os
import csv

# Create file path
filename = 'election_data_2.csv'
filepath = os.path.join('../Data_Files/PyPoll/raw_data', filename)

# open folder with 'with' command and read file using csv.reader
with open(filepath, newline='') as electionfile:
    electiondata = csv.reader(electionfile, delimiter=',')
    # skip header
    next(electiondata)
    # initiate number of votes to zero and candidates that are voted for as an
    # empty array.
    num_votes = 0
    candidate_votes = []
    # loop through each row in the file electiondata
    for row in electiondata:
        # increment number of votes for each row: assumes no duplicates.
        num_votes += 1
        
        candidate_votes.append(row[-1])

votes_per_candidate = {}
candidates = set(candidate_votes)
winning_votes = 0
for candidate in candidates:
    votes = 0
    for vote in candidate_votes:
        if vote == candidate:
            votes += 1
    percent_votes = (votes / num_votes) * 100
    votes_per_candidate[candidate] = [votes, percent_votes]
    if votes > winning_votes:
        winner = candidate
        winning_votes = votes
print('')
print('ELection Results')
print('-------------------')
print('Total Votes: ' + str(num_votes))
print('-------------------')

for candidate in candidates:
    print(
          candidate + ': ' 
          + str(round(votes_per_candidate[candidate][1], 2)) + ' '
          + '(' + str(votes_per_candidate[candidate][0]) + ')'
         )

print('-------------------')
print('Winner: ' + winner)
print('-------------------')
print('')
