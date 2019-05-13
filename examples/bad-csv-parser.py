# from: Daniel Kirsch - Functional Programming in Python
# PyData, Berlin 2016
# https://www.youtube.com/watch?v=r2eZ7lhqzNE
# (formatting mine)

from text import dedent
csv = dedent("""\
    firstName;lastName
    Jim;Drake
    Ben;James
    Tim;Banes
""").strip()

out = [
    { 'firstName':'Jim', 'lastName':'Drake' }
    { 'firstName':'Ben', 'lastName':'James' }
    { 'firstName':'Tim', 'lastName':'Banes' }
]


### from ###


lines = csv.split('\n')
matrix = [
    line.split(';') for line in lines
]
header = matrix.pop(0)
records = []
for row in matrix:
    record = {}
    for index, key in enumerate(header):
        record[key] = row[index]
    records.append(record)


### -or- ###


from operator import methodcaller
from functools import partial

from toolz.curried import map
from toolz.curried import compose

split        = partial(methodcaller, 'split')
split_lines  = split('\n')
split_fields =  split(';')

# Note! toolz's compose is a reverse pipeline
#        (applies the last callable first)

dict_from_keys_vals = compose(
    dict,
    zip,
)

csv_to_matrix = compose(
    map(split_fields),
    split_lines,
)

matrix  = csv_to_matrix(csv)
keys    = next(matrix)
records = map(
    partial(dict_from_keys_vals, keys),
    matrix
)