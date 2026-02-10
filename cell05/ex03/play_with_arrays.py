#!/usr/bin/env python

array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = set()

for value in array:
    if value > 5:
        new_array.add(value + 2)

print(array)
print(new_array)
