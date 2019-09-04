'''
Task
Given a Divisor and a Bound , Find the largest integer N , Such That ,

Conditions :
N is divisible by divisor
N is less than or equal to bound
N is greater than 0.
'''

divisor, bound = 7, 17


def max_multiple(divisor, bound):
    n = bound
    while n > 0:
        if n % divisor == 0:
            return n
            break
        elif divisor > bound:
            return 0
        else:
            n -= 1


print(max_multiple(divisor, bound))
