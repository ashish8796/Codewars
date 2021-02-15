'''
Write a function, persistence, that takes in a positive parameter num 
and returns its multiplicative persistence, which is the number of times
you must multiply the digits in num until you reach a single digit.
'''

import numpy
n = 999


def persistence(n):
    count = 0
    while n >= 10:
        n = numpy.prod([int(i) for i in str(n)])
        count += 1
    return count


print(persistence(n))
