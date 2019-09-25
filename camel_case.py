'''
Write simple .camelCase method for strings. 
All words must have their first letter capitalized without spaces.
'''

string = "camel case method"

def camel_case(string):
    return ''.join(i.title() for i in string.split())


print(camel_case(string))