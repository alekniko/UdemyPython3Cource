dict = {'k1': 5, 'k2': {'subKey1': ['a', 'b', 'c']}}
print(dict)
dict['k2']['subKey1'][1] = dict['k2']['subKey1'][1].upper()

print(dict)
