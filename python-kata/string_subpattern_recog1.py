'''
In this kata you need to build a function to return either true/True or 
false/False if a string can be seen as the repetition of a simpler/shorter subpattern or not.
'''

s = "abababababab"

has_subpattern = lambda s: s in (s*2)[1:-1]

print(has_subpattern(s))