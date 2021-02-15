'''
Scenario
Several people are standing in a row divided into two teams.
The first person goes into team 1, the second goes into team 2, 
the third goes into team 1, and so on.

Task
Given an array of positive integers (the weights of the people), 
return a new array/tuple of two integers, 
where the first one is the total weight of team 1, 
and the second one is the total weight of team 2.
'''

array = [70, 58, 75, 34, 91]


def row_weight(array):
    team1 = 0
    team2 = 0
    for i, weight in enumerate(array, 1):
        if i % 2: team1 += weight
        else: team2 += weight
    return(team1, team2)
            
            



print(row_weight(array))


