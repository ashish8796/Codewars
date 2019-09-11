n =3

def get_double(n):
    return n*2
def create_iterator(get_double, n):
        return get_double(get_double(n))


print(create_iterator(get_double, n))