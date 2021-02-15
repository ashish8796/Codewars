'''
Task
Given an array/list [] of n integers , 
find maximum triplet sum in the array Without duplications .
'''

numbers = [-14, -12, -7, -42, -809, -14, -12]


def max_tri_sum(numbers):
    return sum(sorted(set(numbers))[-3:])


print(max_tri_sum(numbers))
