'''
Exercice
Create a function nextVersion, that will take a string in parameter, 
and will return a string containing the next version number.
'''

version = "1.2.3.4.5.6.7.8"


def next_version(version):
    n_list = version.split('.')
    i = -1
    while (1):
        try:
            string = str(int(n_list[i]) + 1)
            if len(string) == 2:
                n_list[i] = string[-1]
                i -= 1
            else:
                n_list[i] = string
                break
        except IndexError:
            n_list[i + 1] = string
            break
    return '.'.join(i for i in n_list)


print(next_version(version))
