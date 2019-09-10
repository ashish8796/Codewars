'''
Vasya wants to climb up a stair of certain amount of steps (Input parameter 1). 
There are 2 simple rules that he has to stick to.
Vasya can climb 1 or 2 steps at each move.
Vasya wants the number of moves to be a multiple of a certain integer. (Input parameter 2).
Task:
What is the MINIMAL number of moves making him climb to the top of the stairs that satisfies his conditions?
'''
steps, m = 2, 2

def numberOfSteps(steps, m):
    if steps < m:    return (-1)
    else:
        if steps%2:
            con = steps//2 + 1
            while 1:
                if (con / m) .is_integer():     break
                else:   con += 1
        else:
            con = steps//2 
            while 1:
                if (con/m) .is_integer():   break
                else:   con +=1
        return con