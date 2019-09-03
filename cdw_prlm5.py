'''
Definition
A Tidy number is a number whose digits are in non-decreasing order.
Task
Given a number, Find if it is Tidy or not .
'''

n = 9672
def tidyNumber(n):
    return (n == int(''.join(sorted(str(n)))))


print(tidyNumber(n))

