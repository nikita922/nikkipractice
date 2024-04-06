# Input matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Initialize an empty result matrix
result_matrix = []

# Iterate through rows and columns to add corresponding elements
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[0])):
        row.append(matrix1[i][j] + matrix2[i][j])
    result_matrix.append(row)

# Display the result matrix
print("Resultant Matrix:")
for row in result_matrix:
    print(row)
