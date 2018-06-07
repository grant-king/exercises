#Uses functions from inf_monkey with added code to save random words to mp3
#clearly there are better ways to generate random words

import random

def generate_string(length):
    """return a string of 'length' random characters, including space"""
    alphabet = list('abcdefghijklmnopqrstuvwxyz ')
    string = ""
    for it in range(length):
        string = string + random.choice(alphabet)
    return string

def score(goal, test_string):
    """compare two input strings and return decimal value of quotient likeness"""
    #goal = 'methinks it is like a weasel'
    num_equal = 0
    for i in range(len(goal)):
        if goal[i] == test_string[i]:
            num_equal += 1
    return num_equal / len(goal)

def find_words(strings, min_length):
    """find all english words in input list that meet or exceed min_length"""
    lower_words = generate_wordlist()
    made_words = []
    for string_item in strings:
        #break each string into individual literals, stored in clump_list
        clump_list = string_item.split()
        for str_literal in clump_list:
            #add literal to made_words list if it is an english word and >= min_length
            if str_literal.lower() in lower_words and len(str_literal) >= min_length:
                made_words.append(str_literal)
    return made_words

def generate_wordlist():
    """generate and return set of  all english words for fast searching"""
    #must first download nltk data using nltk.download() copy to terminal
    #the very first run to open gui to download required corpus for this function
    #located under the corpus tab, 'words' needs to be dl'd
    #import nltk
    #nltk.download()
    from nltk.corpus import words
    #list of all english words
    word_list = words.words()
    #put lowercased words into a set for fast searching
    return set(word.strip().lower() for word in word_list)

#create an n-member list consisting of lists nn-members long of random strings,
#28 characters each as specified by generate_string()
nn = 1000
n = 10
monkey_strings = [[generate_string(20) for i in range(nn)] for i in range(n)]

text = ['Each of the following',
         'lists are the english words found among lists of',
         'randomly generated', 'character strings.', 'Example string:']
print(text[0], len(monkey_strings), text[1], len(monkey_strings[0]), text[2], len(monkey_strings[0][0]), text[3])
print(text[4], monkey_strings[0][0])

#save tts version of generated words
from gtts import gTTS

long_string = ''
for string_list in monkey_strings:
    print(find_words(string_list, 3))
    for each_word in find_words(string_list, 3):
        long_string = long_string + each_word + " "

print(long_string)
tts = gTTS(long_string)
tts.save('babble.mp3')
