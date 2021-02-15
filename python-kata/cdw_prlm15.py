'''
Given a string, return a new string that has transformed based on the input:
Change case of every character, ie. lower case to upper case, upper case to lower case.
Reverse the order of words from the input.
'''

s = "To be OR not to be That is the Question"


def string_transformer(s):
    return ' '.join(i.swapcase() for i in s.split(' ')[::-1])


print(string_transformer(s))
