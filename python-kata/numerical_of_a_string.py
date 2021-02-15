'''
You are given an input string.
For each symbol in the string if it's the first character occurence, replace it 
with a '1', else replace it with the amount of times you've already seen it...
'''

s = "Hello, World!"

def numericals(s):
    test_s = []
    for i in s:
        if i not in test_s: test_s.append(i)
    d = {i:[j for j in range(1,s.count(i)+1)] for i in test_s}
    string = ''
    for i in s: string += str(d[i][0]); d[i].pop(0)
    return string
    
print(numericals(s))