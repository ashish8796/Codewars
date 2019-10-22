'''
Arthur needs you to return true if he needs to invite more women or false if he is all set.
'''

arr = [1, -1, 1]

def invite_more_women(arr):
    return False if sum(arr)<0 else bool(sum(arr))

print(invite_more_women(arr))