'''
likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
names = ['Alex', 'Jacob', 'Mark', 'Max']
'''

def likes(names):
    if len(names) == 0: return "no one likes this"
    elif len(names) == 1: return f'{names[0]} likes this'
    elif len(names) == 2: return f"{names[0]} and {names[1]} likes this"
    elif len(names) == 3: return f"{names[0]}, {names[1]} and {names[2]} likes this"
    else: return f"{names[0]}, {names[1]} and {len(names[2:])} other likes this"
     

print(likes(names))

