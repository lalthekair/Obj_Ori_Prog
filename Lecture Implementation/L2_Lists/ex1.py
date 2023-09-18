# lst = [[0, 0, 0], [0, 0, 0], [None, None, None]]
lst = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
m = 0
rows = 3
columns = 3
print(lst)
for r in range(rows):  # working on rows. this variable represents each row
    for c in range(columns):  # working on columns. this variable represents each column
        # lst[r][c] = m + 1
        # m += 1
        lst[r][c] = 5
print(lst)
