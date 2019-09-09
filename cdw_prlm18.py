'''
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters 
and numeric digits that occur more than once in the input string. The input string can be 
assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
'''

text = "aabBcde" 

def duplicate_count(text):
    s = text.lower()
    count = 0
    for i in set(s):
        if s.count(i) >= 2:    count +=  1
        else:   continue
    return count


print(duplicate_count(text))



