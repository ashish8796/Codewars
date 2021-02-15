'''
Task
Given an array of N integers, you have to find 
how many times you have to add up the smallest 
numbers in the array until their Sum becomes greater or equal to K.
'''
numbers, value = [19, 98, 69, 28, 75, 45, 17, 98, 67], 464


def minimum_steps(numbers, value):
    sum = 0
    steps = 0
    for i in sorted(numbers):
        sum += i
        steps += 1
        if sum >= value:
            break

    return steps - 1


print(minimum_steps(numbers, value))
