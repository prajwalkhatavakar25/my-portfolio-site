matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
=======
transpose = []

for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transpose.append(row)


print("Transpose Matrix:")
print(transpose)