"""
A nested, or two-dimensional, list is a collection of lists inside a list.
Formula for accessing the second dimension index: list_name[index1][index2]
... where the numbers are the dimension.

The number of elements in the parent two-dimensional list should be the same as the number of rows.
Each row should be one list.

TABLE:
    C1  C2  C3
R1  S   A   D
R2  1   2   3
"""

my_list = [['S', 'A', 'D'], [1, 2, 3]]
for x in range(2):  # number of rows
    for i in range(3):  # number of columns
        print(my_list[x][i])
