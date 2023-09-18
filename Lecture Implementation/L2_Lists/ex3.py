lst2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
rows = 3
columns = 3
for p in range(rows):
    for q in range(columns):

        if q % 2 == 0:
            lst2[p][q] = "even"
        elif q % 2 == 1:
            lst2[p][q] = "odd"
print(lst2)


"""
idea: second loop modifies row 1 in a certain way and row 2 in a different way using if-else.
trace the code and identify the error
trace the code and complete the missing code
"""
