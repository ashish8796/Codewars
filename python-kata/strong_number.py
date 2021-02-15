import math
number = 123

def strong_num(number):
    return "STRONG!!!!" if sum([math.factorial(int(i)) for i in str(number)])==number else "Not Strong !!"

print(strong_num(number))
