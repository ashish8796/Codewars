template = "xxx xxxxx xx","5465253289"
print(template[0], template[1])


def numeric_formatter(template):
    # if len(template[1]) > 1:
    template = list(template)
    lst = []
    for i in template[0].split(' '):
        lst.append(template[1][:len(i)])
        template[1] = template[1].replace(template[1][:len(i)], '')
    print(lst)
    return ' '.join(lst)

print(numeric_formatter(template))

