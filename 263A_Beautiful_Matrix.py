row_index = 0
column_index = 0
for i in range(5):
    row = list(map(int, input().split()))
    if sum(row) == 1:
        row_index = i
        for j in range(5):
            if row[j] == 1:
                column_index = j
            else:
                continue
    else:
        continue
print(abs(row_index-2) + abs(column_index-2))
