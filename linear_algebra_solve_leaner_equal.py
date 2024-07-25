import numpy as np


def get_matrix_from_user(rows, cols):
    matrix = []
    print(
        f"Please enter a {rows}x{cols} matrix, using spaces to separate elements:")
    for i in range(rows):
        row = input(f"Input row {i + 1}: ").split()
        if len(row) != cols:
            print(f"Error: Row {i + 1} must have exactly {cols} elements.")
            return None
        row = [float(num) for num in row]
        matrix.append(row)
    return np.array(matrix)


def get_vector_from_user(size):
    print(
        f"Please enter a vector of size {size}, using spaces to separate elements:")
    vector = input(f"Input vector: ").split()
    if len(vector) != size:
        print(f"Error: Vector must have exactly {size} elements.")
        return None
    vector = [float(num) for num in vector]
    return np.array(vector)


def calculate_determinant(matrix):
    return np.linalg.det(matrix)


def replace_column(matrix, column, index):
    new_matrix = matrix.copy()
    new_matrix[:, index] = column
    return new_matrix


def main():
    # Enter the dimension
    n = int(input("Enter the number of parameters (n): "))

    # Get parameter matrix A
    A = get_matrix_from_user(n, n)
    if A is None:
        return

    # Get the constant vector B
    B = get_vector_from_user(n)
    if B is None:
        return

    # Calculate the determinant of matrix A
    determinant_A = calculate_determinant(A)
    print(f"Determinant of matrix A: {determinant_A}")

    if determinant_A == 0:
        print("Matrix A is singular. No unique solution.")
        return

    # Calculate determinants Dx, Dy, ...
    determinants = []
    for i in range(n):
        Ai = replace_column(A, B, i)
        determinant_Ai = calculate_determinant(Ai)
        determinants.append(determinant_Ai)
        print(
            f"Determinant of matrix A with column {i + 1} replaced: {determinant_Ai}")

    # Solve for variables using Cramer's rule
    x = [det / determinant_A for det in determinants]
    print("Variables:", x)


if __name__ == "__main__":
    main()
