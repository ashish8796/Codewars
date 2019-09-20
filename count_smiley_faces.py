'''
Given an array (arr) as an argument complete the function countSmileys 
that should return the total number of smiling faces.
Valid smiley face examples:
:) :D ;-D :~)
Invalid smiley faces:
;( :> :} :]

'''
arr = [':D',':~)',';~D',':)']

def count_smileys(arr):
    symb = [[':', ';'], ['-', '~',')', 'D']]
    count = 0
    for val in arr:
        if len(val) == 2:
            if val[0] in symb[0] and val[1] in symb[1]: count += 1
        if len(val) == 3:
            if (val[0] in symb[0]) and (val[1] in symb[1] and val[2] in symb[1]): count += 1
    return count
                
                
print(count_smileys(arr))