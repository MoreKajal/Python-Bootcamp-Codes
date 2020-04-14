# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:02:51 2020

@author: Kajal
"""

# Regular expressions are text matching patterns

# re module

import re

patterns = ['term1', 'term2']

text = 'THis is a string with terrm1, but not the otherr term'

re.search('hello', 'hello world')

for pattern in patterns:
    print('Searching for "%s" in : \n "%s" ' %(pattern, text))
    
    #Check for match
    if re.search(pattern, text):
        print( '\n')
        print('Match was found')
        
    else:
        print( '\n')
        print('No Match was found !!')

match = re.search(patterns[0], text)
type(match)       # >> NoneType

match.start()
match.end()
#  Use this match.  to get methods available

split_term = '@'
phrase = 'What is your email, is it hello@gmail.com ?'

re.split(split_term, phrase)
# Split returns a list

'hello world'.split()

# Finding instances of patterns
re.findall('match', 'Here is one match, here is another match')

# multi regular expression finding

def multi_re_find(patterns, phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    
    for pattern in patterns:
        print('Searching the phrase using the re check : %r' %pattern)
        print(re.findall(pattern, phrase))
        print('\n')

##  Repetation syntax

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]

multi_re_find(test_patterns,test_phrase)

# Character Set
#the input [ab] searches for occurrences of either a or b


test_patterns = ['[sd]',    # either s or d
                's[sd]+']   # s followed by one or more s or d

multi_re_find(test_patterns,test_phrase)

## Exclusion
#We can use ^ to exclude terms by incorporating it into the bracket syntax notation.

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

# Use [^!.? ] to check for matches that are not a !,.,?, or space. Add a + to check that the match appears at least once. This basically translates into finding the words.

re.findall('[^!.? ]+',test_phrase)

## Character Ranges
#Common use cases are to search for a specific range of letters in the alphabet. For instance, [a-f] would return matches with any occurrence of letters between a and f.

test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=['[a-z]+',      # sequences of lower case letters
               '[A-Z]+',      # sequences of upper case letters
               '[a-zA-Z]+',   # sequences of lower or upper case letters
               '[A-Z][a-z]+'] # one upper case letter followed by lower case letters
                
multi_re_find(test_patterns,test_phrase)

## Escape Codes
# You can use special escape codes to find specific types of patterns in your data, such as digits, non-digits, whitespace, and more.

test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

multi_re_find(test_patterns,test_phrase)

        