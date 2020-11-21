import os

def clean_file(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)

# Let's try to get better accuracy by cleaning the tweets text
# Define some cleaning methods for the Tweet Text
# Create a function to clean the tweets
import re
import string

def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text

def remove_doublespace(text):
    text = re.sub('  +', ' ', text)
    return text

def clean_twitter_text(text):
    return remove_punct(remove_doublespace(text))

