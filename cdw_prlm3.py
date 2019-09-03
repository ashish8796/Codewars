'''
Task
Given an array/list [] of integers , 
Construct a product array Of same size Such That 
prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].
'''

arr = [16,17,4,3,5,2]


def product_array(numbers):
    prod = []
    for i in arr:
        multiply = 1
        for j in arr:
            if j == i: continue
            else: multiply *= j
        prod.append(multiply)
    return prod


print(product_array(arr))
