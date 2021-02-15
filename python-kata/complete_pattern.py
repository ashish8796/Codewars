'''
Give you two number rows , columns and a string str. Returns a rows x columns table pattern 
and fill in the str(each grid fill in a char, 
the length of str is always less than or equals to the total numbers of grids):
pattern(3, 3, "codewars") should return:
+---+---+---+
| c | o | d |
+---+---+---+
| e | w | a |
+---+---+---+
| r | s |   |
+---+---+---+
'''
rows, columns, s = 3, 3, "codewars"

def pattern(rows, columns, s):
    string = ""
    a = 0
    for i in range(rows*2 +1):
        if i%2 == 0: string += '+---'*columns+'+\n'
        else:
            for j in range(columns):
                if a < len(s): string += f'| {s[a]} '; a += 1
                else: string += '|   '
            string += '|\n'        
    return string.rstrip()
            
                    
                    

print(pattern(rows, columns, s))