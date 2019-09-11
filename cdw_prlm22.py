'''
Complete the function/method that determines if the given array of integers is circularly sorted.
These arrays are circularly sorted (true):
[2, 3, 4, 5, 0, 1]       -->  [0, 1] + [2, 3, 4, 5]
[4, 5, 6, 9, 1]          -->  [1] + [4, 5, 6, 9]
While these are not (false):
[4, 1, 2, 5]
[8, 7, 6, 5, 4, 3]
'''

arr = [1, 2, 3, 4, 5]


def circularly_sorted(arr):
    if arr == sorted(arr):
        return True
    if sorted(arr) == arr[::-1]:
        return False
    for i in range(len(arr)-1):
        if arr[i] > arr[i + 1]:
            ls1 = arr[i+1:]
            ls2 = arr[:i+1]
            break
    if ls1[0] > ls2[0]:
        nl = ls2 + ls1
    else:
        nl = ls1 + ls2
    if sorted(nl) == nl:
        return True
    else:
        return False


print(circularly_sorted(arr))
