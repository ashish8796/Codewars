'''
Write a function that returns the total surface area and volume of a box as an array: [area, volume]
'''

w,h,d = 4, 2, 6

def get_size(w,h,d):
    return [2*(w*h+h*d+d*w), w*h*d]


print(get_size(w,h,d))