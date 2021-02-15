'''
a line of people of having single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. 
Otherwise return NO.
'''

people = [25, 25, 25, 25, 50, 100, 50]


def tickets(people):
    c25, c50, c100 = 0, 0, 0
    for  val in people: 
        if val == 25:  c25 += 1
        elif val == 50:  c25 -= 1;  c50 += 1 
        else:
            if c25 >= 1 and c50 >= 1: c25 -= 1; c50 -= 1; c100 +=1
            elif c25 >= 3: c25 -= 3; c100 +=1
        if abs(c25)!=c25 or abs(c50)!=c50: return "NO"
    if (c25 * 25 + c50 * 50 + c100 * 100) == (25 * len(people)): return "YES"
    else: return "NO"
        

print(tickets(people))