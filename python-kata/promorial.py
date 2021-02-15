n = 2546

def num_primorial(n):
    result, count, num = 2, 1, 3
    while count < n:
        if all(num % i != 0 for i in range(2, num)): result *= num; num += 1; count += 1
        else: num += 1

    return result
            
            
print(num_primorial(n))