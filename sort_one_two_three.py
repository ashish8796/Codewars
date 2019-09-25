import inflect
arr = [9, 99, 999]

def sort_by_name(arr):
    p = inflect.engine()
    d = {p.number_to_words(val): val for val in arr}
    return [d[i] for i in sorted(d)]

print(sort_by_name(arr))    

