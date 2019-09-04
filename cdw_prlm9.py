'''
Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as 
input and that returns the missing letter in the array.
You will always get an valid array. And it will be always 
exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.
'''
import string
chars = ['a', 'b', 'c', 'd', 'f']


def find_missing_letter(chars):
    alpha = string.ascii_lowercase if chars[0] >= 'a' else string.ascii_uppercase
    for char in alpha[alpha.index(chars[0]):]:
        if char not in chars:
            return char


print(find_missing_letter(chars))