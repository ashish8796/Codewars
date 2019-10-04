import math
number = 145

def strong_num(number):
    lst = [math.factorial(int(i)) for i in str(number)]
    if sum(lst) == number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"

print(strong_num(number))