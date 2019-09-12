import sys
import os
import nltk
import csv
INPUT_DIR = 'data'

#nltk.download('punkt')

excluded_punctuation = set(r"""!"#$%&()*+,-/:;<=>?@[\]^_`{|}~""")

for line in sys.stdin:
	for sentence in nltk.sent_tokenize(line):
            sentence = ''.join(ch for ch in sentence if ch not in excluded_punctuation)	
            print(' '.join(nltk.word_tokenize(sentence)).lower())

