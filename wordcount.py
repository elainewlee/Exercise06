from sys import argv
script, filename = argv
#import string

def count_words(filename):
    in_file = open(filename)
    read_file = in_file.read().lower()
    in_file.close()
    replace_file = read_file.replace(".", " ").replace(",", " "). replace("?", " ")
    word_list = replace_file.split()

    dictionary = {}          
    for word in word_list:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    print dictionary

count_words(filename)