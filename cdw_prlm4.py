'''
You are working at a lower league football stadium 
and you've been tasked with automating the scoreboard.
The referee will shout out the score, you have already 
set up the voice recognition module which turns the ref's voice into a string, 
but the spoken score needs to be converted into an array ( or tuple ) for the scoreboard!
e.g. "The score is four nil" should return [4,0]
'''

string = "Arsenal just conceded another goal, two nil"

def scoreboard(string):
    score = ["nil", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return [score.index(i) for i in string.split(' ') if i in score]


print(scoreboard(string))

