'''
It's pretty straightforward. Your goal is to create a function that removes the first and 
last characters of a string. You're given one parameter, the original string. 
You don't have to worry with strings with less than two characters.
'''

s = 'eloquent'

def remove_char(s):
    re = [i for i in s]
    re.pop(0)
    re.pop(-1)
    return "".join(re)

print(remove_char(s))