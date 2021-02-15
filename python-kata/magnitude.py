'''
Task
calculate the sum s of the squared modulus of all complex elements of z if z is in correct form.
Our function sqr-modulus returns a list of three elements
*the first element of this list is a boolean:
 True if z is in correct form ('cart' or 'polar')
 False if z is not in correct form.
*the second element of the list is the sum s of the squared modulus of 
all complex numbers in z if the returned boolean is true, -1 if it is false.
*the third element is the greatest number got by rearranging the digits of s. 
We will admit that the greatest number got from-1 is 1.
'''


z = ['polar', 2, 'b']


def sqr_modulus(z):
    tag = ['cart', 'polar']
    s = 0
    if z[0] in tag and all(type(x) == int for x in z[1:]):
        for i, j in zip(z[1::2], z[2::2]):
            if z[0] == 'cart':
                s += i*i + j*j
            elif z[0] == "polar":
                s += i*i
        y = int("".join(i for i in sorted(str(s))[::-1]))
        if s > y: return (True, s, s) 
        else: return  (True, s, y)
    else:
        return (False, -1, 1)


print(sqr_modulus(z))
