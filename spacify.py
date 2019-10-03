'''
Modify the spacify function so that it returns the given string with spaces inserted between each character.

spacify("hello world") # returns "h e l l o   w o r l d"
'''

string = 'hello world'

def spacify(string):
    return ' '.join(string)

print(spacify(string))