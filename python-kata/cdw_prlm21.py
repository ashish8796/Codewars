'''
A pair of gloves is constituted of two gloves of the same color.
You are given an array containing the color of each glove.
You must return the number of pair you can constitute.
'''

gloves = ["gray","black","purple","purple","gray","black"]

def number_of_pairs(gloves):
    count = 0
    d = {i:gloves.count(i) for i in set(gloves)}
    for i in d:
        if d[i] //2:
            count += d[i] //2
    return count


print(number_of_pairs(gloves))
        