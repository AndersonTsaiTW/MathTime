
import numpy as np


def get_matrix_from_user(rows, cols):
    matrix = []
    print(
        f"Please enter {rows} row {cols} column, use blank to seperate elements:")
    for i in range(rows):
        row = input(f"Input the row {i+1}: ").split()
        row = [float(num) for num in row]  # change to floot
        matrix.append(row)
    return np.array(matrix)


def get_vector_from_user(size):
    vector = []
    print(f"Please enter a vector which size is {size}:")
    row = input(f"Input vector: ").split()
    vector = [float(num) for num in row]  # change to floot
    return np.array(vector)


def main():
    # enter the dimension
    n = int(input("Enter the paramaters' number (n): "))

    # get paramater matrix A
    A = get_matrix_from_user(n, n)

    # get the const B
    B = get_vector_from_user(n)

    # solve the variable
    try:
        x = np.linalg.solve(A, B)
        print("Variables:", x)
    except np.linalg.LinAlgError:
        print("Matrix A is singular. No result.")


if __name__ == "__main__":
    main()
