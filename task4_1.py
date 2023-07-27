# Напишите функцию для транспонирования матрицы

def transpose(matrix):
    a = len(matrix)
    b = len(matrix[0])
    transposed_matrix = [[0 for _ in range(a)] for _ in range(b)]
    for i in range(a):
        for j in range(b):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


matrix = [[11, 22, 33],
          [44, 55, 66],
          [77, 88, 99]]
print(f'матрица:{matrix}')
transposed_matrix = transpose(matrix)
print(f'транспонированная матрица:{transposed_matrix}')
