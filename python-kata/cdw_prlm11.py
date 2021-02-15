'''
The goal of this exercise is to convert a string to a new string where each 
character in the new string is "(" if that character appears only once in the 
original string, or ")" if that character appears more than once in the original
 string. Ignore capitalization when determining if a character is a duplicate.
 '''

word = "Success"


def duplicate_encode(word):
    return ''.join(")" if word.lower().count(i) > 1 else "(" for i in word.lower())


print(duplicate_encode(word))
