rows = [[1, 2, 3]]

for row_i in range(1, 51):
    rows.append([])
    rows[-1].append(rows[-2][0])
    for val_i in range(len(rows[-2]) - 1):
        rows[-1].append(rows[-2][val_i] + rows[-2][val_i + 1])
    rows[-1].append(rows[-2][-1])

print(rows[49][39])
