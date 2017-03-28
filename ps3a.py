import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTERS_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
                           'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
                           'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
                           'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
                           }
##YET TO ASSIGN RIGHT VALUES FOR THE SCRABBLE_LETTERS_VALUE


#HELPER FUNCTION
## This helper prints thw number of words. This is done by parsing the
##words.txt into inFile and reading line by line to strip the spaces and
##get the length of the wordlist

WORDLIST_FILENAME = "words.txt"
def load_words():
    """
    returns a lsit of valid words. Words are strings of lowercase letters.
    Depending on the size if the word list, this function may take a while
    to finish
    """

    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
        print " ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence and
    the values are the integer counts, for the number of times that an
    element is repeated in the sequence.

    sequence: string or list

    return:dictionary
    """
##freq: dictionary(element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

##(end of the helper code)
##------------------------------------------------------
#
#Problem #1: Scoring a word

def get_word_score(word, n):
    """
     Returns the score for a word. Assumes the word is a valid word.

     The score for a word is the sum of the points for letters in the word
     multiplied by the length of the word, plus 50 points if all n letters
     are used on the first go.

     Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth
     3, and so forth

     word: string (lowercase letters)
     returns: int >= 0

     
    
