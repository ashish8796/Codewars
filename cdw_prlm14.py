'''
Could you make a program that
makes this string uppercase
gives it sorted in alphabetical order by last name.
'''
s = 'Ashish:Kumar;Praven:saini;Deepak:dubey'


def meeting(s):
    return ''.join('({}, {})'.format(i[0], i[1]) for i in sorted([j.upper().split(':')[::-1] for j in s.split(';')]))


print(meeting(s))
