import numpy as np


def matrix_operations():
    # Create two 2x2 matrices
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])

    print("Matrix 1:")
    print(matrix1)
    print("\nMatrix 2:")
    print(matrix2)

    # Matrix addition
    print("\nMatrix Addition:")
    print(matrix1 + matrix2)

    # Matrix subtraction
    print("\nMatrix Subtraction:")
    print(matrix1 - matrix2)

    # Matrix multiplication
    print("\nMatrix Multiplication:")
    print(np.dot(matrix1, matrix2))

    # Matrix transpose
    print("\nTranspose of Matrix 1:")
    print(matrix1.T)

    # Matrix determinant
    print("\nDeterminant of Matrix 1:")
    print(np.linalg.det(matrix1))

    # Matrix inverse
    print("\nInverse of Matrix 1:")
    print(np.linalg.inv(matrix1))


if __name__ == "__main__":
    matrix_operations()
