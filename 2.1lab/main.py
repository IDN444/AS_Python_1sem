#пункт а
def sum_values(x):
    total = sum(x.values())
    return total
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(sum_values(dict))

#пункт б
def list_dict(x):
    dict = {}
    for item in x:
        dict[item] = {}
    return dict
list = ['a', 'b', 'c']
print(list_dict(list))

#пункт в
def values_equal(x):
    values = list(x.values())
    return all(y == values[0] for y in values)
dict = {'a': 1, 'b': 1, 'c': 1}
print(values_equal(dict))
