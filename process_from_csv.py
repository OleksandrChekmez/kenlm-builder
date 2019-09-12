import sys
import os
import nltk
import csv
#INPUT_DIR = 'data'

#nltk.download('punkt')

excluded_punctuation = set(r"""!"#$%&()*+,-/:;<=>?@[\]^_`{|}~""")

#print('reading ',os.path.join(INPUT_DIR, sys.argv[1]))

with open(os.path.join(sys.argv[1]), newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='"')
     for row in spamreader:
         for sentence in nltk.sent_tokenize(', '.join(row)):
            sentence = ''.join(ch for ch in sentence if ch not in excluded_punctuation)	
            print(' '.join(nltk.word_tokenize(sentence)).lower())

