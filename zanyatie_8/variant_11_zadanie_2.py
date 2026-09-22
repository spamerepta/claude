def read_matrix():
    rows = int(input())
    return [list(map(int, input().split())) for i in range(rows)]


def find_max(matrix):
    best_i, best_j = 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > matrix[best_i][best_j]:
                best_i, best_j = i, j
    return best_i, best_j


def print_matrix(matrix):
    for row in matrix:
        print(*row)


a = read_matrix()
b = read_matrix()
ai, aj = find_max(a)
bi, bj = find_max(b)
a[ai][aj], b[bi][bj] = b[bi][bj], a[ai][aj]
print_matrix(a)
print()
print_matrix(b)
