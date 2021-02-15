'''
Write a function named first_non_repeating_letter that takes a string input, 
and returns the first character that is not repeated anywhere in the string.
For example, if given the input 'stress', the function should return 't', 
since the letter t only occurs once in the string, and occurs first in the string.
As an added challenge, upper- and lowercase letters are considered the same character, 
but the function should return the correct case for the initial letter. For example, 
the input 'sTreSS' should return 'T'.
'''

s = 'agiisgsiigs'

def first_non_repeating_letter(s):
    if all(s.count(i)>1 for i in s):
            return ''
    for i in s:
        if s.lower().count(i.lower()) == 1:
            return i

print(first_non_repeating_letter(s))