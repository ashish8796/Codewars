'''
Task
Given an array/list [] of integers , 
Construct a product array Of same size Such That 
prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].
'''

arr = [8778, 219450, 219450, 11550, 8778, 3325, 31350]


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
