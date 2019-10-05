'''
Determine the area of the largest square that can fit inside a circle with radius r.
'''
r = 7

def area_largest_square(r):
    return round(((2*r)/(2**.5))**2)

print(area_largest_square(r))