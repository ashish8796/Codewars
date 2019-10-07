'''
Complete the function that returns an array of length n, starting with the given number 
x and the squares of the previous number. If n is negative or zero, return an empty array/list.
'''

x , n = 2, 5

def squares(x, n):
    res = []
    if n<=0:
        return []
    else:
        for i in range(n):
            if i == 0:
                res.append(x)
            else:
                res.append(res[-1]**2)
    return res

print(squares(x, n))