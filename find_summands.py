'''
In this Kata, you will be given a number n (where n >= 1) and your 
task is to find n consecutive odd numbers whose sum is exactly the cube of n.
Mathematically:
cube = n ** 3
sum = a1 + a2 + a3 + ..... + an
sum == cube
a2 == a1 + 2, a3 == a2 + 2, .......
For example:
find_summands(3) = [7,9,11] # because 7 + 9 + 11 = 27, the cube of 3. 
Note that there are only n = 3 elements in the array.
'''

n = 1
def find_summands(n):
    ls = []
    x = (n**3- n*(n-1))/ n
    while len(ls) < n: ls.append(x); x += 2
    return ls

print(find_summands(n))