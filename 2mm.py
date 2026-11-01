#1---- Matrix multiplication ---



import timeit

def matrix_multiply(A, B):
    return [
        [
            sum(A[i][k] * B[k][j] for k in range(len(B)))
            for j in range(len(B[0]))
        ]
        for i in range(len(A))
    ]

# Input dimensions
rA, cA = map(int, input("Enter rows and columns of A: ").split())
rB, cB = map(int, input("Enter rows and columns of B: ").split())

if cA != rB:
    print("Matrix multiplication is not possible.")
else:
    print("Enter Matrix A:")
    A = [list(map(int, input().split())) for _ in range(rA)]

    print("Enter Matrix B:")
    B = [list(map(int, input().split())) for _ in range(rB)]

    result = matrix_multiply(A, B)

    print("Result:")
    for row in result:
        print(row)

    execution_time = timeit.timeit(
        lambda: matrix_multiply(A, B),
        number=10000
    )

    print("Execution time:", execution_time)




#2----Strassem matrix ---

import timeit

def add(A, B):
    n = len(A)
    return [
        [A[i][j] + B[i][j] for j in range(n)]
        for i in range(n)
    ]

def subtract(A, B):
    n = len(A)
    return [
        [A[i][j] - B[i][j] for j in range(n)]
        for i in range(n)
    ]

def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, subtract(B12, B22))
    M4 = strassen(A22, subtract(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(subtract(A21, A11), add(B11, B12))
    M7 = strassen(subtract(A12, A22), add(B21, B22))

    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    result = [
        C11[i] + C12[i] for i in range(mid)
    ] + [
        C21[i] + C22[i] for i in range(mid)
    ]

    return result


n = int(input("Enter matrix size (power of 2): "))

print("Enter Matrix A:")
A = [list(map(int, input().split())) for _ in range(n)]

print("Enter Matrix B:")
B = [list(map(int, input().split())) for _ in range(n)]

result = strassen(A, B)

print("Result:")
for row in result:
    print(row)

execution_time = timeit.timeit(
    lambda: strassen(A, B),
    number=10000
)

print("Execution time:", execution_time)




#3 Matrix using Numpy



import timeit
import numpy as np

def matrix_multiply():
    A = [[1, 2], [3, 4]]
    B = [[1, 2], [3, 4]]

    return np.dot(A, B)

result = matrix_multiply()

print("Result:")
for row in result:
    print(row)

execution_time = timeit.timeit(
    stmt=matrix_multiply,
    number=100
)

print("Execution time:", execution_time)
