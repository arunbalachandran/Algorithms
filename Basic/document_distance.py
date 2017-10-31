from collections import defaultdict
import string
import sys
import time

string_translation_table = str.maketrans(string.punctuation
                                         + string.ascii_uppercase,
                                         ' '*len(string.punctuation)
                                         + string.ascii_lowercase)

def clean_words(text_file):
    word_count = defaultdict(lambda: 0)
    with open(text_file) as fp:
        text = fp.read()
    text = text.translate(string_translation_table)
    for word in text.split():
        word_count[word] += 1
    return word_count

def document_distance(filename1, filename2):
    cleaned_file1 = clean_words(filename1)
    cleaned_file2 = clean_words(filename2)
    sum_doc = 0.0
    magnitude1, magnitude2 = 0.0, 0.0
    for word in cleaned_file1:
        if word in cleaned_file2:
            sum_doc += cleaned_file1[word] * cleaned_file2[word]
    magnitude1 = sum(map(lambda i: cleaned_file1[i]**2, cleaned_file1))**0.5
    magnitude2 = sum(map(lambda i: cleaned_file2[i]**2, cleaned_file2))**0.5
    return sum_doc / (magnitude1 * magnitude2)

if __name__ == '__main__':
    filename1, filename2 = sys.argv[1], sys.argv[2]
    start_time = time.time()
    dist = document_distance(filename1, filename2)
    end_time = time.time() - start_time
    print('Distance is', dist)
    print('Time taken is', end_time)
