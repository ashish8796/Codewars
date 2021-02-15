'''
In this example you have to validate if a user input string is alphanumeric.
The string has the following conditions to be alphanumeric:
At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore
'''

import re
password = "PassW0rd"

def alphanumeric(password):
    pattern = r"^[A-Za-z0-9]+$"
    if re.search(pattern, password):
        return True 
    else:
        return False


print(alphanumeric(password))