# Import a text file filled with a paragraph of your choosing.

# Assess the passage for each of the following:

#     Approximate word count

#     Approximate sentence count

#     Approximate letter count (per word)

#     Average sentence length (in words)

# Example output:

# Paragraph Analysis
# -----------------
# Approximate Word Count: 122
# Approximate Sentence Count: 5
# Average Letter Count: 4.56557377049
# Average Sentence Length: 24.4

import os
import csv
from statistics import mean

# Sets file path
filename = 'paragraph_2.txt'
filepath = os.path.join('../Data_Files/PyParagraph/raw_data', filename)

with open(filepath, newline='\n') as parfile:
    # using csv.reader with delimiter equal to a space the script is seperated
    # by word.  this allows for easy word counts.
    pardata = csv.reader(parfile, delimiter=' ')

    # Initialize empty list for counts
    # num = number of words per row
    # w_per_sentence = number of words per sentence
    # word_length = number of leters per word
    num = []
    w_per_sentence = []
    word_length = []
    # Initialize initial values for number of sentences and words per sentence
    # counters.
    num_sentence = 0
    word_sent_count = 0
    # loop through rows
    for row in pardata:
        # determine if row is not empty
        if row:
            # if row is not empty count number of words in a row
            num.append(len(row))
            # loop through row for each word.
            for word in row:
                # determine if word contains a sentence ending punctuation.
                if '.' in word or '?' in word or '!' in word:
                    # determine the puctuation '.' was not used as an initial
                    # sentence count can be thrown off by abrieviations that 
                    # contain a more than one period with no space (A.B.).
                    if len(word) > 2:
                        # increment number of sentences by one
                        num_sentence += 1
                        # increment word in sentence counter by 1.
                        # append counter to words per sentence list.
                        # reset counter to 0
                        word_sent_count += 1
                        w_per_sentence.append(word_sent_count)
                        word_sent_count = 0
                        # append the length or word minus one to acount for the 
                        # puctuation.
                        word_length.append(len(word)-1)

                else:
                    # increment word per sentence count
                    word_sent_count += 1
                    # determine if word contains ',', ':', or ';'
                    if ',' in word or ';' in word or ':' in word:
                        # appent length of word minus one to account for 
                        # punctuation
                        word_length.append(len(word)-1)
                    else:
                        # append length of word.
                        word_length.append(len(word))

# determine number of words
num_words = sum(num)
# determine average number of leters in word rounded to two decimal places
avg_word_length = round(mean(word_length), 2)
# determine average sentence lenght in words
avg_sent_length = mean(w_per_sentence)
# print analysis results
print('number of words: ' + str(num_words))
print('number of sentences: ' + str(num_sentence))
print('average letter count: ' + str(avg_word_length))
print('average sentence length: ' + str(avg_sent_length))