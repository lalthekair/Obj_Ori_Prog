# 1) nested list, so nested loop. 2) random number generator
# need to import library first before code

import random
lst = [[0, 0, 0], [0, 0, 0]]
# if we were to remove the last sublist, we would get an index out of range error since no. of rows is 2 now, not 3

rows = 2
columns = 3
for r in range(rows):
    for c in range(columns):
        lst[r][c] = random.randint(1, 5000)  # name_of_library.name_of_method
print(lst)
