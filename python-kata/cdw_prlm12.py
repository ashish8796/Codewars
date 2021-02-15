'''
Write a function that takes an array of numbers (integers for the tests) and a target number. 
It should find two different items in the array that, when added together, give the target value. 
The indices of these items should then be returned in a tuple like so: (index1, index2).
'''

n, t = [1234, 5678, 9012], 14690


def two_sum(n, t):
    return [(i, j) for i, val1 in enumerate(n) for j, val2 in enumerate(n[1:], 1) if val1+val2 == t][0]



print(two_sum(n, t))
